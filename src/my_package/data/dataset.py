#Imports
import numpy as np
from PIL import Image
import json

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms = None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation = annotation_file
        self.trfms = transforms
        with open(self.annotation,'r') as f:
            jsonll = list(f)
        list_datatemp = []
        for i in jsonll:
            list_datatemp.append(json.loads(i))
        self.list_data = list_datatemp

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.list_data)

    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_png_ann: the segmentation annotation image (in the form of a numpy array) (shape: (1, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each 
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            doing the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image, png segmentation and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the arrays would be (3, H, W) and (1, H, W), respectively.
            3. Scale the values in the arrays to be with [0, 1].
            4. Perform the desired transformations on the image.
            5. Return the dictionary of the transformed image and annotations as specified.
        '''
        #extracting the image and the annoatation image
        data_ind = self.list_data[idx]
        image_at_ind = Image.open('/home/jatin/Desktop/20CS10087_Assign-4/tests/data/'+data_ind["img_fn"])
        img_at_index_asarray = np.asarray(image_at_ind)
        ann_img = Image.open('/home/jatin/Desktop/20CS10087_Assign-4/tests/data/'+data_ind["png_ann_fn"])
        ann_img_asarr = np.asarray(ann_img)
        
        #aaplying the required transformations on the image
        if self.trfms:
            for transf in self.trfms:
                img_at_index_asarray = transf(img_at_index_asarray)
        img_at_index_asarray = img_at_index_asarray/255
        ann_img_asarr = ann_img_asarr/255
        img_at_index_asarray = img_at_index_asarray.transpose(2,0,1)

        #dictionary to be returned
        diction = dict()
        diction["image"] = img_at_index_asarray
        diction["gt_png_ann"] = ann_img_asarr
        gtb = []
        bbox = data_ind["bboxes"]
        for bb in bbox:
            gtb.append([bb["category"],bb["bbox"][0],bb["bbox"][1],bb["bbox"][2],bb["bbox"][3]])
        diction["gt_bboxes"] = gtb
        return diction


        
