import cv2

image = cv2.imread('img/test3.png', 0)
(H,W) = image.shape

centerH = int(H/2)
centerW = int(W/2)

im1 = image[:centerH, :centerW] #fb, fb
im2 = image[:centerH, centerW:] #fb, bf
im3 = image[centerH:, :centerW] #bf, fb
im4 = image[centerH:, centerW:] #bf, bf

images = [im1, im2, im3, im4]