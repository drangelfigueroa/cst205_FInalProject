from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import file
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, IMAGES, configure_uploads
import forms
import os
global filename

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootrap = Bootstrap(app)

app.config['UPLOADED_IMAGES_DEST'] = '/static/uploads/'
images = UploadSet('images', IMAGES)
configure_uploads(app, images)


@app.route('/', methods=['GET', 'POST'])
def index():
    global filename
    filename = None
    form = forms.UploadImage()
    if form.validate_on_submit():
        filename = secure_filename(form.img.data.filename)
        form.img.data.save('static/uploads/' + filename)
    return render_template('index.html', form=form, img=filename)
