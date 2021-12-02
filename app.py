from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, IMAGES, configure_uploads
import forms
import os
import manipulations as man

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.config['UPLOADED_IMAGES_DEST'] = '/static/uploads/'
images = UploadSet('images', IMAGES)
configure_uploads(app, images)


@app.route('/', methods=['POST', 'GET'])
def index():
    form = forms.UploadImage()
    # Gets file name and saves file
    if form.validate_on_submit():
        man.img_name = secure_filename(form.img.data.filename)
        form.img.data.save('static/uploads/' + man.img_name)

        ## test function in manipulations.py
        man.test()
    # Removes image
    if 'rm' in request.form:
        os.remove(f'static/uploads/{man.img_name}')
        man.img_name = None
    return render_template('index.html', form=form, img=man.img_name)
