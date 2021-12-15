# CST207 - Final Project
# Time: Fall 2021
# Date: 13-Dec.-2021
# School: CSUMB
# Author: Team 795
# Description: Application to convert IMG to an edited version based on user's choosing
#########################################################################################
"""
 All of our image manipulation functions should go here.

 img_name: name of unedited image.
 edited_name: name of edited image.
"""
from PIL import Image, ImageFilter, ImageOps
import cv2
import os
import numpy as np

global img_name, edited_name
img_name = None
edited_name = None

# List of manipulations.
# This list will populate the dropdown and
# call your function.

# Format: (String for dropdown, function name)
MANIPULATIONS = [('Black & White', 'bnw'), ('Blur', 'blur'), ('Contour', 'contour'), ('Edge Enhance', 'edge_enhance'),
                ('Emboss', 'emboss'), ('Face Detect', 'faces'), ('Find Edges','find_edges'), ('Mirror Flip', 'hRef'), 
                ('Scale Up', 'upScale'), ('Scale Down', 'downScale'), ('Sepia', 'sepia'), ('Smooth', 'smooth'), 
                ('Red Intensity', 'red'), ('Green Intensity', 'green'), ('Blue Intensity', 'blue'), ('Negative', 'neg'),
                ('Grey Scale', 'greyScale'), ('Image Contrast', 'contrast'), ('Image Blurry', 'blurry')]

####################################################
# List of Functions
####################################################
def call_function(selected):
    """
        Will call function by itself. No need to add anything
        to app.py. Just append tuple to MANIPULATIONS 
    """
    for name in MANIPULATIONS:
        if(name[0] == selected):
            globals()[name[1]]()

########################################################
# Function
# Action: Formula for detecting the faces in IMG
########################################################
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

########################################################
# Sub-function
# Action: Formula for Every pixel change into Sepia
# Location: Sepia Function
########################################################
def sepia_getpixel(pixel):
    if pixel[0] < 63:
        r, g, b = int(pixel[0]*1.1), pixel[1], int(pixel[2]*.9)
    elif pixel[0] > 62 and pixel[0] < 192:
        r, g, b = int(pixel[0]*1.15), pixel[1], int(pixel[2]*.85)
    else:
        r = int(pixel[0]*1.08)
        if r > 255:
            r = 255
        g, b = pixel[1], pixel[2]//2
    return r, g, b

########################################################
# Function
# Action: Formula for scaling down the IMG
########################################################
def downScale():
    """ scale down image """
    global img_name, edited_name
    im = Image.open(f'static/uploads/{img_name}')

    w = im.width//2
    h = im.height//2

    im = im.resize((w, h))

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

########################################################
# Function
# Action: Formula for scaling up the IMG
########################################################
def upScale():
    """ scale up image """
    global img_name, edited_name
    im = Image.open(f'static/uploads/{img_name}')

    w = im.width*2
    h = im.height*2

    im = im.resize((w, h))
    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

########################################################
# Function
# Action: Formula for converting IMG to Black & White
########################################################
def bnw():
    """ converts to black and white """
    global img_name, edited_name
    im = Image.open(f'static/uploads/{img_name}')

    im = im.convert('1')
    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

########################################################
# Function
# Action: Formula to flipping IMG over the X-axis
########################################################
def hRef():
    """ Reflects the image on the 'X' axis """
    global img_name, edited_name
    im = Image.open(f'static/uploads/{img_name}')
    im = ImageOps.mirror(im)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

########################################################
# Function
# Action: Formula to edit IMG with Sepia
########################################################
def sepia():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')

    sepia_list = map(sepia_getpixel, im.getdata())
    im.putdata(list(sepia_list))

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

########################################################
# Function
# Action: Formula to clear IMG
########################################################
def rm_img():
    """Helper function to clear image"""
    global img_name
    if img_name:
        os.remove(f'static/uploads/{img_name}')
        img_name = None

########################################################
# Function
# Action: Formula to clear editied IMG
########################################################
def rm_edited():
    """Helper function to clear edited image"""
    global edited_name
    if edited_name:
        os.remove(f'static/uploads/{edited_name}')
        edited_name = None

########################################################
# Function
# Action: Formula to blur the IMG
########################################################
def blur():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.BLUR)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

########################################################
# Function
# Action: Formula to contour the IMG
########################################################
def contour():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.CONTOUR)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

########################################################
# Function
# Action: Formula to emboss the IMG
########################################################
def emboss():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.EMBOSS)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

########################################################
# Function
# Action: Formula to find edges the IMG
########################################################
def find_edges():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.FIND_EDGES)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

########################################################
# Function
# Action: Formula to enhance edges the IMG
########################################################
def edge_enhance():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

########################################################
# Function
# Action: Formula to smoothen the IMG
########################################################
def smooth():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.SMOOTH_MORE)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

########################################################################################################################
# Function
# Action: Changes the intensity of the RGB colors
# Description: color_id is either 0, 1, or 2 depending on if its red, green, or blue (i.e. 0 = red, 1 = green, 2 = blue)
#               intensity ranges from 0 to beyond with 0 removing all of that value. You multiply all of the rgb values 
#               by the amount of intesity
#########################################################################################################################
def rgb_intensity(color_id, intensity):
    global img_name, edited_name
    img = Image.open(f'static/uploads/{img_name}')
    intensity_list = []
    for i in img.getdata():
        temp_rgb = list(i)
        temp_rgb[color_id] *= intensity
        intensity_list.append(tuple(temp_rgb))
    
    img.putdata(list(intensity_list))
    edited_name = f'edited_{img_name}'
    img.save(f'static/uploads/{edited_name}')

def red():
    rgb_intensity(0, 2)
def green():
    rgb_intensity(1, 2)
def blue():
    rgb_intensity(2, 2)

####################################################
# Function
# Action: Edit IMG into GrayScale
####################################################
def greyScale():
    global img_name, edited_name
    print("Okay")
    img = cv2.imread(f'static/uploads/{img_name}', cv2.IMREAD_GRAYSCALE)

    edited_name = f'edited_{img_name}'
    cv2.imwrite(f'static/uploads/{edited_name}', img)

####################################################
# Function
# Action: Edit IMG with Negative filter
####################################################
def neg():
    global img_name, edited_name
    img = cv2.imread(f'static/uploads/{img_name}')

    img_not = cv2.bitwise_not(img)

    edited_name = f'edited_{img_name}'
    cv2.imwrite(f'static/uploads/{edited_name}', img_not)

####################################################
# Function
# Action: Edit IMG with IMG Contrast Filter
####################################################
def contrast():
    global img_name, edited_name
    img = cv2.imread(f'static/uploads/{img_name}')
    contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)

    edited_name = f'edited_{img_name}'
    cv2.imwrite(f'static/uploads/{edited_name}', contrast_img)

####################################################
# Function
# Action: Edit IMG with IMG Blurry
####################################################
def blurry():
    global img_name, edited_name
    img = cv2.imread(f'static/uploads/{img_name}')
    blur_image = cv2.GaussianBlur(img, (7,7), 0)

    edited_name = f'edited_{img_name}'
    cv2.imwrite(f'static/uploads/{edited_name}', blur_image)


# END OF CODE
