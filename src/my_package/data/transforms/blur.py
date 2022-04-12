#Imports
import numpy as np
from PIL import Image, ImageFilter

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''

        #code
        self.radius = radius

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''

        #code 
        image_tb = Image.fromarray(image)
        blurred_image = image_tb.filter(ImageFilter.GaussianBlur(self.radius))
        image_asarray = np.asarray(blurred_image)
        return image_asarray

