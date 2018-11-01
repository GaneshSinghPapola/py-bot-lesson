from flask import request, jsonify, g

from ..api import api
from ..models.users import User
from ..utils.auth import generate_token, requires_auth, verify_token
from flask_uploads import UploadSet, configure_uploads, IMAGES

photos = UploadSet('photos', IMAGES)


@api.route("/user", methods=["GET"])
@requires_auth
def get_user():
    return jsonify(result=g.current_user)


@api.route("/create_user", methods=["POST"])
def create_user():
    incoming = request.form
    print(incoming)
    user = User({'email': incoming["email"], 'firstname': incoming["firstname"],
                'lastname': incoming["lastname"], 'password': User.hashed_password(
        incoming["password"])})


    try:
        user.save()
        if 'image' in request.files:
            photos.save(request.files['image'])
            return jsonify(message = "saved successfully"), 200

    except Exception:
        print (Exception)
        return Exception

    new_user = User.find_one({'email': incoming["email"]})
    return jsonify(
        id = str(new_user['_id']),
        token = generate_token(new_user)
    )


@api.route("/double", methods=["POST"])
def double_number():
    r = request.get_json()

    try:
        number = r["number"]
    except (KeyError, TypeError):
        return jsonify({"error": "no number passed"}), 400

    try:
        double = int(number)*2
    except ValueError:
        return jsonify({"error": "a number was not passed"}), 400

    return jsonify({"double": double}), 200
    
@api.route("/register", methods = ["POST"])
def register_user():
    user=request.get_json(force = True)

    obj=User({'email': user["email"], 'firstname': user["firstname"],
                'lastname': user["lastname"], 'password': User.hashed_password(user["password"])})
    print(request)
    # return "saved successfully"

    try:
        obj.save()
        if 'image' in request:
            photos.save(user['image'])
            return jsonify(message = "saved successfully"), 200

    except Exception:
        print (Exception)
        return Exception


@api.route("/get_token", methods = ["POST"])
def get_token():
    incoming=request.get_json()
    user=User.get_user_with_email_and_password(
        incoming["email"], incoming["password"])
    if user:
        return jsonify(token = generate_token(user))

    return jsonify(error = True), 403


@api.route("/is_token_valid", methods = ["POST"])
def is_token_valid():
    incoming=request.get_json()
    is_valid=verify_token(incoming["token"])

    if is_valid:
        return jsonify(token_is_valid = True)
    else:
        return jsonify(token_is_valid = False), 403




# @api.route('/upload', methods=['GET', 'POST'])
# def upload():
#     print("images in uplaosd asdasdasd  ")

#     if request.method == 'POST' and 'image' in request.files:
#         filename = photos.save(request.files['image'])
#         return jsonify(message="saved successfully"), 200
