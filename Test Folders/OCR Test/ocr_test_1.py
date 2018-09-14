import cv2
import sys
import pytesseract
import datetime

# testing the speed of tesseract on a 1080p resolution screenshot of a display filled with text
img = cv2.imread('test3.png', 1)
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# img_size = img.size()

for i in range(20):
	start = datetime.datetime.now()
	pytesseract.image_to_string(img)
	fin = datetime.datetime.now()
	n = fin-start
	print(n)
	



cv2.waitKey()
cv2.destroyAllWindows()