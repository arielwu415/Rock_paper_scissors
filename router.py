from flask import Blueprint, flash, render_template, request
from werkzeug.utils import secure_filename

router = Blueprint(__name__, 'router')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

@router.route('/')
def home():
    return render_template('index.html')


@router.route('/', methods = ['GET', 'POST'])
def upload_img():
    if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'