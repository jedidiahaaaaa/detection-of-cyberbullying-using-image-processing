#importing packages
from imutils.object_detection import non_max_suppression #convenience functions for openCV, simplifying the commands from openCV
from imutils import resize #resize the image
import numpy as np
import time
import cv2


#constructing argument parser and parsing the arguments
#easier managing image testings

east = 'frozen_east_text_detection.pb' #importing the EAST text detector model file path
newW = 320
newH = 320

#loading the image
image = cv2.imread('img/test3.png', 1)

#creating an image copy and getting the dimensions of the image
orig_image = image.copy()
(H, W) = image.shape[:2]

#ratio of the original image in comparison to the new image dimesions
rH = H * float(newH) #east only works on image size of multiples of 32
rW = W * float(newW) 

#resizing the image into the new dimension
image = cv2.resize(image, (newH, newW))
(H, W) = image.shape[:2]

#define the two output layers for the EAST detector model we are interested in
#one to output probabilities
#one to derive bounding box coordinates of the text
layerNames = [
	"feature_fusion/Conv_7/Sigmoid",
	"feature_fusion/concat_3"
]

#loading the trained EAST text detector
print("[INFO] loading EAST text detector")
net = cv2.dnn.readNet(east)

centerH = int(H/2)
centerW = int(W/2)

im1 = image[:centerH, :centerW] #fb, fb
im2 = image[:centerH, centerW:] #fb, bf
im3 = image[centerH:, :centerW] #bf, fb
im4 = image[centerH:, centerW:] #bf, bf

images = [im1, im2, im3, im4]

for img in images:
	#creating a blob from the image
	#performing a forward pass of model to get the output two outputs from the layers
	blob = cv2.dnn.blobFromImage(img, 1.0, (W,H), (123.68, 116.78, 103.94), swapRB=True, crop=False) #pre-trained RGB mean values
	start = time.time()
	net.setInput(blob)
	(scores, geometry) = net.forward(layerNames)
	end = time.time()
	#show time taken to get the blob
	print("[INFO] text detection took {:.6f} seconds".format(end-start))
	






cv2.imshow('img', image)


cv2.waitKey()
cv2.destroyAllWindows()