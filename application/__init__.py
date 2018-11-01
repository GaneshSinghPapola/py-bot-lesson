import os
from flask import Flask, request, url_for, redirect, g
from flask_bcrypt import Bcrypt
from flask_restful import Api
# from flask_cors import CORS

# from .utils.auth import generate_token, requires_auth, verify_token

from config import app_config
app = Flask(__name__)
bcrypt = Bcrypt()
bcrypt.init_app(app)
from flask_uploads import UploadSet, configure_uploads, IMAGES
from .api.users import photos
app.config.from_object(app_config["development"])
# app.config.from_pyfile('config.py')


# CORS(app, resources={r"/*": {"origins": "*"}})
@app.route("/", methods=["GET"])
def index():
    return "server works"




UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOADED_PHOTOS_DEST'] = UPLOAD_FOLDER
configure_uploads(app, photos)


from .api import api as apidb
app.register_blueprint(apidb, url_prefix='/api/v1')
