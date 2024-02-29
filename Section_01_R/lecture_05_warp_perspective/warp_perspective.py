import cv2
import numpy as np

image = cv2.imread("../Images/cards.jpg")

cv2.imshow("Original Image", image)

width, height = 500, 500

pt1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])

pt2 = np.float32([[0,0],[width,0],[0,height], [width, height]])

matrix = cv2.getPerspectiveTransform(pt1, pt2)

imgOutput = cv2.warpPerspective(image, matrix, (width, height))

cv2.imshow("Output Image", imgOutput)
cv2.waitKey(0)