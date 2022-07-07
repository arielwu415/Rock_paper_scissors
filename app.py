import os
from flask import Flask
from werkzeug.utils import secure_filename
from router import router

UPLOAD_FOLDER = '/images/training_reaources/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.register_blueprint(router, url_prefix='/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(debug=True, port=8000)