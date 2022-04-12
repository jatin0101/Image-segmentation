#Imports
import numpy as np
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        # code
        self.tupleb = isinstance(output_size, tuple)
        self.output_size = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        #code
        image_orig = Image.fromarray(image)
        if self.tupleb:
            rescale_image = image_orig.resize(self.output_size)
            return np.asarray(rescale_image)
        else:
            height = image.shape[0]
            width = image.shape[1]
            ar = width/height
            if (height<width):
                rescale_image = image_orig(int(self.output_size*ar),self.output_size)
                return np.asarray(rescale_image)
            else:
                rescale_image = image_orig(self.output_size,int(self.output_size/ar))
                return np.asarray(rescale_image)
       

