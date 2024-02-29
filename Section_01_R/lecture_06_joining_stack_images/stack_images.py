import cv2
import numpy as np

image1 = cv2.imread("../Images/cards.jpg")
im1_resized = cv2.resize(image1,(318, 159))

print("Image 1 Shape", image1.shape)
image2 = cv2.imread("../Images/image2.jpg")

print("Image 2 shape: ", image2.shape)
imageHorizontalStack = np.hstack((im1_resized, image2))
imageVerticallStack = np.vstack((im1_resized, image2))

cv2.imshow("Horizontal Stack", imageHorizontalStack)
cv2.imshow("Vertical Stack", imageVerticallStack)

cv2.waitKey(0)