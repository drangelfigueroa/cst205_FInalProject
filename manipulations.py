"""
 All of our image manipulation functions should go here.

 img_name: name of unedited image.
 edited_name: name of edited image.
"""
from PIL import Image, ImageFilter
import cv2
import os

global img_name, edited_name
img_name = None
edited_name = None

# List of manipulations.
# This list will populate the dropdown and
# call your function.

# Format: (String for dropdown, function name)
MANIPULATIONS = [ ('Blur', 'blur'), ('Contour', 'contour'), ('Edge Enhance', 'edge_enhance'),
('Emboss', 'emboss'), ('Face Detect', 'faces'), ('Find Edges', 'find_edges'), ('Sepia', 'sepia'),
('Smooth', 'smooth')]




def call_function(selected):
    """
        Will call function by itself. No need to add anything
        to app.py. Just append tuple to MANIPULATIONS 
    """
    for name in MANIPULATIONS:
        if(name[0]==selected):
            globals()[name[1]]()

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

def upScale():
    """ scale up image """
    global img_name, edited_name
    im = Image.open(f'static/uploads/{img_name}')

    w = im.width()//2
    h = im.height()//2

    im = im.resize(w,h)

    im.save(f'static/uploads/{edited_name}')
    
def downScale():
    """ scale down image """
    global img_name, edited_name
    im = Image.open(f'static/uploads/{img_name}')

    w = im.width()*2
    h = im.height()*2

    im = im.resize(w,h)

    im.save(f'static/uploads/{edited_name}')
    
def bnw():
    """ converts to black and white """
    global img_name, edited_name
    im = Image.open(f'static/uploads/{img_name}')

    im = im.convert('1') 

    im.save(f'static/uploads/{edited_name}')
    
def hRef():
    """ Reflects the image on the 'X' axis """
    global img_name, edited_name
    im = Image.open(f'static/uploads/{img_name}')
    im = ImageOps.mirror(im)

    im.save(f'static/uploads/{edited_name}')

def sepia():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')

    sepia_list = map(sepia_getpixel, im.getdata())
    im.putdata(list(sepia_list))

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')


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

def blur():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.BLUR)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

def contour():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.CONTOUR)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

def emboss():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.EMBOSS)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

def find_edges():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.FIND_EDGES)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

def edge_enhance():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')

def smooth():
    global img_name, edited_name

    im = Image.open(f'static/uploads/{img_name}')
    im = im.filter(ImageFilter.SMOOTH_MORE)

    edited_name = f'edited_{img_name}'
    im.save(f'static/uploads/{edited_name}')
