from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, IMAGES, configure_uploads
import forms
import os

global img_name

img_name = None
SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
# bootrap = Bootstrap(app)

app.config['UPLOADED_IMAGES_DEST'] = '/static/uploads/'
images = UploadSet('images', IMAGES)
configure_uploads(app, images)


@app.route('/', methods=['POST', 'GET'])
def index():
    global img_name
    form = forms.UploadImage()
    # Gets file name and saves file
    if form.validate_on_submit():
        img_name = secure_filename(form.img.data.filename)
        form.img.data.save('static/uploads/' + img_name)
    # Removes image
    if 'rm' in request.form:
        os.remove(f'static/uploads/{img_name}')
        img_name = None
    return render_template('index.html', form=form, img=img_name)
