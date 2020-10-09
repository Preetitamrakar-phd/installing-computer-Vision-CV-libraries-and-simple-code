import cv2
img = cv2.imread("pythonlogo.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayImage.jpg", grayImg)
cv2.imshow("originalImage",img)
cv2.imshow("GrayImage",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindow()
