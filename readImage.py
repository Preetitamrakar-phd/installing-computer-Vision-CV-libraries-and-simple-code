import cv2  #importing library
img = cv2.imread ("pythonlogo.jpg") #reading image and storing in variable
cv2.imshow("logo", img) #display image
cv2.imwrite("logo1.png", img) #write and save the image (name, var)
cv2.waitKey(0)   #0 means infinite time it will show
cv2.destroyAllWindows() # closing every figure
