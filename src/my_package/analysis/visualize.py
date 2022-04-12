#Imports
import numpy as np
from PIL import Image,ImageDraw,ImageFont
#import matplotlib.pyplot as plot

def plot_visualization(outputp,outputp1,image,pred_boxes,pred_masks,pred_class,pred_score): # Write the required arguments

  # The function should plot the predicted segmentation maps and the bounding boxes on the images and save them.
  # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.

  #storing the index of top-3 predictions if number of predictions is greater than 3
  index = []
  if(len(pred_score)>3):
    pred_scores_cc = pred_score.copy()
    pred_scores_cc.sort(reverse = True)
    for i in range(3):
      index.append(pred_score.index(pred_scores_cc[i]))
  else:
    for i in range(len(pred_score)):
      index.append(i)
  
  image_edit = image.copy()
  image_edit_bb = image.copy()

  #changing the image to H*W*3
  image_edit = image_edit.transpose((1,2,0))
  image_edit_bb = image_edit_bb.transpose(1,2,0)
  
  #applying the segmentation masks on the image.
  
  pred_masks[0] = pred_masks[0].transpose((1,2,0))
  image_edit = image_edit + pred_masks[0]*[0,0,0.5]
  if(len(index)>1):
    pred_masks[1] = pred_masks[1].transpose(1,2,0)
    image_edit = image_edit + pred_masks[1]*[0,0.5,0]
  if(len(index)>2):
    pred_masks[2] = pred_masks[2].transpose(1,2,0)
    image_edit = image_edit + pred_masks[2]*[0.5,0,0]
  
  #Storing the image with segmentation masks
  image_asimg = Image.fromarray((image_edit*255).astype(np.uint8))
  image_asimg.save(outputp)

  #drawing the boundary boxes and the writing the corressponding labels on the image.
  image_asimg_bb = Image.fromarray((image_edit_bb*255).astype(np.uint8))
  draw = ImageDraw.Draw(image_asimg_bb)
  font = ImageFont.load_default()
  for i in index:
    (y1,x1),(y2,x2) = pred_boxes[i]
    draw.rectangle([y1,x1,y2,x2],outline='green',width=2)
    draw.text((y1,x2),pred_class[i],font=font, fill=(0,0,255))

  #saving the image with bounding boxes in the given output path.
  image_asimg_bb.save(outputp1)
  return image_edit,image_edit_bb
