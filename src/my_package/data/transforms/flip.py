#Imports

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

        # code
        if(flip_type == 'horizontal'):
            self.hori = True
        else:
            self.hori = False
        
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        #code
        flip_image = image.copy()
        height = flip_image.shape[0]
        width = flip_image.shape[1]
        #swapping the pixels to flip the image
        if self.hori:
            for i in range((int)(width/2)):
                for j in range(height):
                    flip_image[j][i][0],flip_image[j][width-i-1][0] = flip_image[j][width-i-1][0],flip_image[j][i][0]
                    flip_image[j][i][1],flip_image[j][width-i-1][1] = flip_image[j][width-i-1][1],flip_image[j][i][1]
                    flip_image[j][i][2],flip_image[j][width-i-1][2] = flip_image[j][width-i-1][2],flip_image[j][i][2]
        else:
            for i in range((int)(height/2)):
                for j in range(width):
                    flip_image[i][j][0],flip_image[height-1-i][j][0] = flip_image[height-1-i][j][0],flip_image[i][j][0]
                    flip_image[i][j][1],flip_image[height-1-i][j][1] = flip_image[height-1-i][j][1],flip_image[i][j][1]
                    flip_image[i][j][2],flip_image[height-1-i][j][2] = flip_image[height-1-i][j][2],flip_image[i][j][2]
        return flip_image


       