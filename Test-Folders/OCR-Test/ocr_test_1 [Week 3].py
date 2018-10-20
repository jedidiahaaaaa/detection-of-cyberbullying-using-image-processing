import cv2
import sys
import pytesseract
import datetime

# testing on how to get multiple resolutions
img = cv2.imread('test3.png', 1)
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# img_size = img.size()
res1 = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
res2 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
res3 = cv2.resize(img, (600,600))
cv2.imshow('img',img)
cv2.imshow('res1',res1)
cv2.imshow('res2',res2)
cv2.imshow('res3',res3)

# for i in range(20):
# 	start = datetime.datetime.now()
# 	pytesseract.image_to_string(img)
# 	fin = datetime.datetime.now()
# 	n = fin-start
# 	print(n)
	



cv2.waitKey()
cv2.destroyAllWindows()