import cv2
import numpy as np

image = cv2.imread('../Images/documentscanner2.jpg')

kernel = np.ones((5,5), np.uint8)

# Setting the threshold values
t_lower = 400
t_higher = 500

# Apply canny edge detector
imgCanny = cv2.Canny(image, t_lower, t_higher)

# Dilation of image

imageDilation = cv2.dilate(imgCanny, kernel, iterations=1)

# Erosion of Image
imageErosion = cv2.erode(imageDilation, kernel, iterations=1)

cv2.imshow("Original Image", image)

cv2.imshow("Canny Image", imgCanny)

cv2.imshow("Image Dilation", imageDilation)

cv2.imshow("Image Erosion", imageErosion)

cv2.waitKey(0)