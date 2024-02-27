import cv2

image = cv2.imread('../Images/lambo.png')

imgBlur = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imshow("Original Image", image)

cv2.imshow("Blur Image", imgBlur)

cv2.waitKey(0)