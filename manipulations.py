"""
 All of our image manipulation functions should go here.

 img_name: name of unedited image.
 edit_name: name of edited image.
"""
global img_name, edit_name
img_name = None


def test():
    # calls global variables
    global img_name, edited_name

    # How edited image should be saved as in static/upluads
    edited_name = f'edited_{img_name}'

    # Prints in console
    print(f'Unedited: {img_name}\nedited: {edited_name}')
