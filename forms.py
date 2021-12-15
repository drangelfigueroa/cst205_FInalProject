# CST207 - Final Project
# Time: Fall 2021
# Date: 13-Dec.-2021
# School: CSUMB
# Author: Team 795
# Description: Application to convert IMG to an edited version based on user's choosing
#########################################################################################
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

images = UploadSet('images', IMAGES)


class UploadImage(FlaskForm):
    img = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, 'Images only!')
    ])
# END OF CODE
