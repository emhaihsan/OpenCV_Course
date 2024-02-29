import cv2
import numpy as np

# This is grayscale because we olny have 512 x 512 pixels
# image = np.zeros((512,512))

# If we want to add the color functionality, we need to add channel
image = np.zeros((512,512,3))

# Add color
image[:] = 255, 255, 255

# Draw a line
cv2.line(image, (0,0), (image.shape[1],image.shape[0]),(0,255,0),3)

# Draw a rectangle
cv2.rectangle(image, (0,0), (250,350), (0,0,255), 10)

# Draw a Cricle
cv2.circle(image, (400,50), 30, (0,255,255), 3)

# Write Text on an Image
cv2.putText(image, "OpenCV", (300,200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,150,0), 5)
cv2.imshow("Output Image", image)

cv2.waitKey(0)