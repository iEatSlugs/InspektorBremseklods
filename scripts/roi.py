import cv2 as cv
import numpy as np

img = cv.imread(r"c:\Users\PC User\Pictures\testbilleder\billede_2.jpg")
x_start, y_start, x_end, y_end = 0, 260, 1090, 390

def klip_roi(img):
    x_start, y_start, x_end, y_end = 0, 260, 1090, 390
    return img[ y_start:y_end, x_start:x_end]

def linjer_roi(img):
   
    cv.line(img, (0, y_start), (1280, y_start), (0, 0, 255), 2)
    cv.line(img, (0, y_end), (1280, y_end), (0, 0, 255), 2)

 
img = cv.imread(r"c:\Users\PC User\Pictures\testbilleder\billede_2.jpg")
cv.imshow(r"c:\Users\PC User\Pictures\testbilleder\billede_2.jpg", img)
cv.waitKey(0)
cv.destroyAllWindows()