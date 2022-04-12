#Imports
import numpy as np
from PIL import Image

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''

        # code
        self.shape = shape
        self.crop_type = crop_type
        if(crop_type == 'center'):
            self.randomcrop = False
        else:
            self.randomcrop = True

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # code
        image_cc = image.copy()
        height_n = self.shape[0]
        width_n = self.shape[1]
        height_orig = image_cc.shape[0]
        width_orig = image_cc.shape[1]
        if self.randomcrop:
            for i in range(height_orig):
                for j in range(width_orig):
                    if i<=height_n and j<=width_n:
                        continue
                    else:
                        image_cc[i][j][0] = 255
                        image_cc[i][j][1] = 255
                        image_cc[i][j][2] = 255
            return image_cc
        else:
            left = (width_orig-width_n)/2
            right = (width_n+width_orig)/2
            top = (height_orig-height_n)/2
            bottom = (height_orig+height_n)/2
            image_asimg = Image.fromarray(image_cc)
            cropped_image = image_asimg.crop(left,top,right,bottom)
            cropped_image_asarray = np.asarray(cropped_image)
            return cropped_image_asarray

        

 