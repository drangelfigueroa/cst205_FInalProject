"""
 All of our image manipulation functions should go here.

 img_name: name of unedited image.
 edit_name: name of edited image.
"""
import numpy as np
import cv2
import os

global img_name, edit_name
img_name = None
edited_name = None

# List of manipulations.
# This list will populate the dropdown and
# call your function. *Append new function names*
MANIPULATIONS = ['Face Detect']


def faces():
    """ Face Detection algorithm """
    global img_name, edited_name
    casc_class = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(casc_class)

    # Pull image and comvert to grayscale
    img = cv2.imread(f'static/uploads/{img_name}')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Face Algorithm
    faces = face_cascade.detectMultiScale(gray, 1.1, 9)

    # Rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # SAVE
    edited_name = f'edited_{img_name}'
    cv2.imwrite(f'static/uploads/{edited_name}', img)


def rm_img():
    """Helper function to clear image"""
    global img_name
    if img_name:
        os.remove(f'static/uploads/{img_name}')
        img_name = None


def rm_edited():
    """Helper function to clear edited image"""
    global edited_name
    if edited_name:
        os.remove(f'static/uploads/{edited_name}')
        edited_name = None
