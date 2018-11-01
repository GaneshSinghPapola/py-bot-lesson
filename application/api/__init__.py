from flask import Blueprint, jsonify

api = Blueprint('api_db', __name__)

# from . import users, dialog
from ..api.users import *
from ..api.dialog import *

@api.errorhandler(403)
def forbidden(error):
    print("403 response reached")
    pass
    #return render_template('errors/403.html', title='Forbidden'), 403

@api.errorhandler(404)
def page_not_found(error):
    print("404 response reached")
    pass
    #return render_template('errors/404.html', title='Page Not Found'), 404

@api.errorhandler(400)
def route_not_found(error):
    print("400 response reached")
    pass
    #return render_template('errors/404.html', title='Page Not Found'), 400    

@api.errorhandler(405)
def method_not_allowed(error):
    print("405 response reached")
    pass
    #return jsonify(message="Method Not Allowed for the requested URLee."), 401

@api.errorhandler(500)
def internal_server_error(error):
    print("500 response reached")
    pass
    # return render_template('errors/500.html', title='Server Error'), 500

@api.before_request
def before_request():

    pass
    # check for Idle time & expiration
    # flask.g.user = current_user