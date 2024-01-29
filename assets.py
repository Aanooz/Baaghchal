import os
import  sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Assets(object):
    def __init__(self):
        self.blank_image_path = "images/blanks/blank_64x64.png"
        self.tiger_image_path = "images/tigers/tigerr.png"
        self.goat_image_path = "images/goats/goatt.png"
        self.configuration_path = "settings.conf"

        #set correct path to the images
        self.blank_image_path = resource_path(self.blank_image_path)
        self.tiger_image_path = resource_path(self.tiger_image_path)
        self.goat_image_path = resource_path(self.goat_image_path)
        self.configuration_path = resource_path(self.configuration_path)

