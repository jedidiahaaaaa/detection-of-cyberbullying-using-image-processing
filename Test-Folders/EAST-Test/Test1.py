#importing packages
from imutils.object_detection import non_max_suppression #convenience functions for openCV, simplifying the commands from openCV
from imutils import resize #resize the image
import numpy as np
import argparse
import time
import cv2


#constructing argument parser and parsing the arguments
#easier managing image testings

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="img/test3.png",
	help="path to input image")
ap.add_argument("-east", "--east", type=str, default="frozen_east_text_detection.pb",
	help="path to input EAST text detector")
ap.add_argument("-c", "--min-confidence", type=float, default=0.5,
	help="minimum probability required to inspect a region")
ap.add_argument("-w", "--width", type=int, default=320,
	help="resized image width (should be multiple of 32)")
ap.add_argument("-e", "--height", type=int, default=320,
	help="resized image height (should be multiple of 32)")
args = vars(ap.parse_args())

#loading the image
image = cv2.imread(args["image"])
#creating an image copy and getting the dimensions of the image
orig = image.copy()
(H, W) = image.shape[:2]

(newW, newH) = (args["width"], args["height"])
#ratio of the original image in comparison to the new image dimesions
rW = W / float(newW)
rH = H / float(newH) #east only works on image size of multiples of 32

#resizing the image into the new dimension
image = cv2.resize(image, (newW, newH))
(H, W) = image.shape[:2]

#define the two output layers for the EAST detector model we are interested in
#one to output probabilities
#one to derive bounding box coordinates of the text
layerNames = [
	"feature_fusion/Conv_7/Sigmoid",
	"feature_fusion/concat_3"]

#loading the trained EAST text detector
print("[INFO] loading EAST text detector...")
net = cv2.dnn.readNet(args["east"])



#creating a blob from the image
#performing a forward pass of model to get the output two outputs from the layersffice
blob = cv2.dnn.blobFromImage(image, 1.0, (W, H), 
	(123.68, 116.78, 103.94), swapRB=True, crop=False) #pre-trained RGB mean values
start = time.time()
net.setInput(blob)
(scores, geometry) = net.forward(layerNames)
end = time.time()

#show time taken to get the blob
print("[INFO] text detection took {:.6f} seconds".format(end-start))

#gets rows and columns from the scores
#initialize set of bounding box rectangle and its corresponding confidence scores
(numRows, numCols) = scores.shape[2:4]
rects = []
confidences = []

#loop with the amount of rows
for y in range(0, numRows):
	#extract the scores(probabilities of text
	#followed by geometric data used to get the potential bounding box coordinates to surround the text
	scoresData = scores[0, 0, y]
	xData0 = geometry[0, 0, y]
	xData1 = geometry[0, 1, y]
	xData2 = geometry[0, 2, y]
	xData3 = geometry[0, 3, y]
	anglesData = geometry[0, 4, y]

	for x in range(0, numCols):
		print("" + str(scoresData[x]))
		if scoresData[x] < args["min_confidence"]:
			continue

		(offsetX, offsetY) = (x * 4.0, y * 4.0)

		angle = anglesData[x]
		cos = np.cos(angle)
		sin = np.sin(angle)

		#using geometry volume to get the width and height of the bounding box
		h = xData0[x] + xData2[x]
		w = xData1[x] + xData3[x]

		#calculate the starting and ending coordinates for the text prediction box
		endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
		endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
		startX = int(endX - w)
		startY = int(endY - h)

		#add the coordinates and probability scores to its lists
		rects.append((startX, startY, endX, endY))
		confidences.append(scoresData[x])

#apply non-maxima suppression to suppress weak and overlapping boxes from the coordinates
boxes = non_max_suppression(np.array(rects), probs=confidences)

#loop through the bounding boxes
for (startX, startY, endX, endY) in boxes:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

	#scaling the bounding boxes based on the ratios
	startX = int(startX * rW)
	startY = int(startY * rH)
	endX = int(endX * rW)
	endY = int(endY * rH)

	#drawing a rectangle on the original size image as the bounding box
	cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)

cv2.imshow('smaller image', image)
cv2.imshow('original image', orig)


cv2.waitKey(0)
# cv2.destroyAllWindows()