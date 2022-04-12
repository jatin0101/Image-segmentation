#Imports
import numpy as np
from PIL import Image

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
    
        self.degrees = degrees

    def __call__(self, sample):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        image_orig = Image.fromarray(sample)
        rotated_img = image_orig.rotate(self.degrees, Image.NEAREST, expand=1)
        return np.asarray(rotated_img)