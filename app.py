# CST207 - Final Project
# Time: Fall 2021
# Date: 13-Dec.-2021
# School: CSUMB
# Author: Team 795
# Description: Application to convert IMG to an edited version based on user's choosing
#########################################################################################
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, IMAGES, configure_uploads
import forms
import manipulations as man
import os

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.config['UPLOADED_IMAGES_DEST'] = '/static/uploads/'
images = UploadSet('images', IMAGES)
configure_uploads(app, images)


@app.route('/', methods=['POST', 'GET'])
def index():
    img = None
    form = forms.UploadImage()
    # Gets file name and saves file
    if form.validate_on_submit():
        man.img_name = secure_filename(form.img.data.filename)
        form.img.data.save('static/uploads/' + man.img_name)

    # Removes image
    if 'rm' in request.form:
        man.rm_img()
        man.rm_edited()

    if 'manip' in request.form:
        manipulation(request.form['manip'])

    if man.edited_name:
        img = man.edited_name
    elif man.img_name:
        img = man.img_name

    return render_template('index.html', form=form, img=img, manipulations=man.MANIPULATIONS)


def manipulation(selected):
    """
        Calls function from manipulations.py
    """
    if (selected == 'None'):
        man.rm_edited()
    else:
        man.call_function(selected)
# END OF CODE
