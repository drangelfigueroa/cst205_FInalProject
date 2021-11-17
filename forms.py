from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

images = UploadSet('images', IMAGES)


class UploadImage(FlaskForm):
    img = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, 'Images only!')
    ])
