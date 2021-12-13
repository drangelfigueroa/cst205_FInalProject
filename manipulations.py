"""
 All of our image manipulation functions should go here.

 img_name: name of unedited image.
 edit_name: name of edited image.
"""
import numpy as np
import cv2
import os
from PIL import Image
import pytesseract

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = 'System_path_to_tesseract.exe'

global img_name, edit_name
img_name = None
edited_name = None

# List of manipulations.
# This list will populate the dropdown and
# call your function. *Append new function names*
MANIPULATIONS = ['Face Detect', 'Gray Scale', 'Sepia Filter', 'Negative Filter']

####################################################
# List of Functions
####################################################
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

########################################################
# Sub-function
# Action: Formula for Every pixel change into GrayScale
# Location: GrayScale Function
########################################################
def rgb2gray(p):
    new_red = int(p[0] * 0.2989)
    new_green = int(p[1] * 0.5870)
    new_blue = int(p[2] * 0.1140)
    gray = new_red + new_green + new_blue
    return (gray,) * 3

####################################################
# Function
# Action: Edit IMG into GrayScale
####################################################
def grayscale():
    global img_name, edited_name
    print("Okay")
    img = cv2.imread(f'static/uploads/{img_name}', cv2.IMREAD_GRAYSCALE)

    edited_name = f'edited_{img_name}'
    cv2.imwrite(f'static/uploads/{edited_name}', img)

####################################################
# Function
# Action: Edit IMG with Sepia filter
####################################################
### (Daniel Did This Code)

########################################################
# Sub-function
# Action: Formula for Every pixel change Negative filter
# Location: Negative filter Function
########################################################
def rgb2neg(self, pixel):
    return tuple(map(lambda a : 255 - a, pixel))

####################################################
# Function
# Action: Edit IMG with Negative filter
####################################################
def negative():
    global img_name, edited_name
    img = cv2.imread(f'static/uploads/{img_name}')

    img_not = cv2.bitwise_not(img)

    edited_name = f'edited_{img_name}'
    cv2.imwrite(f'static/uploads/{edited_name}', img_not)
