####### REQUIRED IMPORTS FROM THE PREVIOUS ASSIGNMENT #######

from socket import MsgFlag
from src.my_package.analysis.visualize import plot_visualization
from src.my_package.model import InstanceSegmentationModel
from src.my_package.data import Dataset
from src.my_package.analysis import plot_visualization
from src.my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage

####### ADD THE ADDITIONAL IMPORTS FOR THIS ASSIGNMENT HERE #######
from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

# Define the function you want to call when the filebrowser button is clicked.
def fileClick(clicked, dataset, segmentor):

	####### CODE REQUIRED (START) #######
	# This function should pop-up a dialog for the user to select an input image file.
	# Once the image is selected by the user, it should automatically get the corresponding outputs from the segmentor.
	# Hint: Call the segmentor from here, then compute the output images from using the `plot_visualization` function and save it as an image.
	# Once the output is computed it should be shown automatically based on choice the dropdown button is at.
	# To have a better clarity, please check out the sample video.

	#global variable to store the location of the image.
	global image_loc

	image_loc = filedialog.askopenfilename(title='Select image',initialdir='./',filetypes=(('image files','*.jpg'),('All files','*.*')))

	#to display the selected file location in the entry widget.
	loc.set(image_loc)

	#if no image file provided
	if not image_loc:
		return
	
	image_asjpg = Image.open(image_loc)
	image_as_arr = np.array(image_asjpg)/255
	image_as_arr = np.rollaxis(image_as_arr, 2, 0)			#converting to 3*H*W from H*W*3
	pred_boxes,pred_masks,pred_class,pred_score = segmentor(image_as_arr)

	#storing the generated images in the below file locations
	image_seg_fl = '/home/jatin/Desktop/20CS10087_Assign-4/tests/outputs/image_segmented/img_segmented.jpg'
	image_bb_fl = '/home/jatin/Desktop/20CS10087_Assign-4/tests/outputs/image_bb/img_bb.jpg'
	plot_visualization(image_seg_fl,image_bb_fl,image_as_arr,pred_boxes,pred_masks,pred_class,pred_score)

	####### CODE REQUIRED (END) #######

# `process` function definition starts from here.
# will process the output when clicked.
def process(clicked):
	#print("entered process function")
	####### CODE REQUIRED (START) #######
	# Should show the corresponding segmentation or bounding boxes over the input image wrt the choice provided.
	# Note: this function will just show the output, which should have been already computed in the `fileClick` function above.
	# Note: also you should handle the case if the user clicks on the `Process` button without selecting any image file.
	
	#To erase the previous displayed images
	for widget in Picture_frame.winfo_children():
		widget.destroy()
	
	#If the file location is not given by the user.
	if not image_loc:
		print("No image selected! Please select image location")
		error_msg = Label(Picture_frame,text = "No image selected! Please select image location")
		error_msg.grid(row=2, column=1)
		return

	image = Image.open(image_loc)				#Original image.
	image_disp = ImageTk.PhotoImage(image)		#Using the PhotoImage widget to display the images.
	image_label = Label(Picture_frame,image=image_disp)	    #Label to print the image in the Picture_frame
	image_label.image = image_disp

	#If segmented option is chosen from the drop down menu.
	if clicked.get() == "Segmentation":
		
		img_loc = '/home/jatin/Desktop/20CS10087_Assign-4/tests/outputs/image_segmented/img_segmented.jpg'
		image_rsl = Image.open(img_loc)						#Image with segmentation masks
		image_disp2 = ImageTk.PhotoImage(image_rsl)		   
		image_label2 = Label(Picture_frame,image=image_disp2)			   #label to display the image
		image_label2.image = image_disp2
		image_label.grid(row=2,column=0)				   #position of the original image
		image_label2.grid(row=2,column=1)				   #position of the image with segmentation masks

	#If bounding box is chosen.	
	else:
		image_loc_bb = '/home/jatin/Desktop/20CS10087_Assign-4/tests/outputs/image_bb/img_bb.jpg'
		image_rsl_2 = Image.open(image_loc_bb)			  #Image with boundung boxes
		image_disp2 = ImageTk.PhotoImage(image_rsl_2)
		image_label2 = Label(Picture_frame,image = image_disp2)
		image_label2.image = image_disp2
		image_label.grid(row=2,column=0)
		image_label2.grid(row=2,column=1)				#Position of the image with boundung boxes
	
	####### CODE REQUIRED (END) #######

# `main` function definition starts from here.
if __name__ == '__main__':

	####### CODE REQUIRED (START) ####### (2 lines)
	# Instantiate the root window.
	root = Tk()
	root.title('Image processor')

	#Frame for displaying images
	Picture_frame = Frame(root)
	Picture_frame.grid(row=2,column=0)
	# Provide a title to the root window.
	
	####### CODE REQUIRED (END) #######

	# Setting up the segmentor model.
	annotation_file = '/home/jatin/Desktop/20CS10087_Assign-4/tests/data/annotations.jsonl'
	transforms = []

	# Instantiate the segmentor model.
	segmentor = InstanceSegmentationModel()
	# Instantiate the dataset.
	dataset = Dataset(annotation_file, transforms=transforms)

	
	# Declare the options.
	options = ["Segmentation", "Bounding-box"]
	clicked = StringVar()
	clicked.set(options[0])

	loc = StringVar(None)						#To store the file location so that it can be dispayed on the Entry widget
	e = Entry(root, width=70, textvariable=loc)
	e.grid(row=0, column=0)

	####### CODE REQUIRED (START) #######
	# Declare the file browsing button
	
	image_loc = None
	file_bb = Button(root,text = "Browse",command=partial(fileClick,clicked,dataset,segmentor))
	
	####### CODE REQUIRED (END) #######

	####### CODE REQUIRED (START) #######
	# Declare the drop-down button
	opt_button = OptionMenu(root,clicked,*options)		
	####### CODE REQUIRED (END) #######

	# This is a `Process` button
	myButton = Button(root, text="Process", command=partial(process, clicked))

	#placing all the components
	file_bb.grid(row=0, column=1)
	opt_button.grid(row=0,column=2)	
	myButton.grid(row=0, column=3)
	

	####### CODE REQUIRED (START) ####### (1 line)
	# Execute with mainloop()
	root.mainloop()
	####### CODE REQUIRED (END) #######