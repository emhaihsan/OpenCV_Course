import cv2

image = cv2.imread("../Images/lambo.png")

print("Original image shape: " ,image.shape)
#-----> 1000 ---> resize image width
#-----> 650 ----> resize image height
image_resize = cv2.resize(image, (1000, 650))

print("Resized Shape: ", image_resize.shape)

cv2.imshow("Original Image", image)

cv2.imshow("Resize Image", image_resize)

cv2.waitKey(0)