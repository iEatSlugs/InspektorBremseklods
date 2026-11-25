import cv2
 

img = cv2.imread(r"c:\Users\PC User\Pictures\testbilleder\billede_3.jpg")

x_start, y_start, x_end, y_end = 0, 250, 1090, 399


cv2.line(img, (0, y_start), (1280, y_start), (0, 0, 255), 2)
cv2.line(img, (0, y_end), (1280, y_end), (0, 0, 255), 2)
 
# Show the original and cropped images
cv2.imshow(r"c:\Users\PC User\Pictures\testbilleder\billede_3.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()