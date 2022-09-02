from tkinter import Frame
import cv2
from cv2 import imshow
from cv2 import imwrite
from cv2 import waitKey
from cv2 import destroyWindow

cam_port = 1
cam = cv2.VideoCapture(cam_port)
  
# reading the input using the camera
result, image = cam.read()
  
# If image will detected without any error, 
# show result
if result:
  
    # showing result, it take frame name and image 
    # output
    imshow("GeeksForGeeks", image)
  
    # saving image in local storage
    imwrite("GeeksForGeeks.png", image)
  
    # If keyboard interrupt occurs, destroy image 
    # window
    waitKey(0)
    destroyWindow("GeeksForGeeks")
  
# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")