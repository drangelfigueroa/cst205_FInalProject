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
def rgb2gray(self, p):
    new_red = int(p[0] * 0.2989)
    new_green = int(p[1] * 0.5870)
    new_blue = int(p[2] * 0.1140)
    gray = new_red + new_green + new_blue
    return (gray,) * 3

####################################################
# Function
# Action: Edit IMG into GrayScale
####################################################
def grayscale(self, path):
    global img_name, edited_name
    img = cv2.imread(f'static/uploads/{img_name}')

    gray_list = map(self.rgb2gray, img.getdata())
    img.putdata(list(gray_list))

    cv2.imwrite(f'static/uploads/{edited_name}', img)

####################################################
# Function
# Action: Edit IMG with Sepia filter
####################################################
def sepia(self, path):
    global img_name, edited_name
    img = cv2.imread(f'static/uploads/{img_name}')

    sepia_list = []
    for i in img.getdata():
        new_val = (0.3 * i[0] + 0.59 * i[1] + 0.11 * i[2])
        new_red = int(new_val * 2)

        if new_red > 255:
            new_red = 255
        new_green = int(new_val * 1.5)
        if new_green > 255:
            new_green = 255
        new_blue = int(new_val)
        if new_blue > 255:
            new_blue = 255

        sepia_list.append((new_red, new_green, new_blue))
    img.putdata(sepia_list)
    cv2.imwrite(f'static/uploads/{edited_name}', img)

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
def negative(self, path):
    global img_name, edited_name
    img = cv2.imread(f'static/uploads/{img_name}')

    negative_list = map( self.rgb2neg, img.getdata() )
    img.putdata(list(negative_list))
    cv2.imwrite(f'static/uploads/{edited_name}', img)
