import cv2

img = cv2.imread('2.jpg')
img = cv2.resize(img, (512, 512))
blur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
cv2.imshow('source', img)
fine = (img - median)
cv2.imshow('0.5 fine', fine)

img = img + fine

cv2.imshow('Sharpen', img)
cv2.waitKey()