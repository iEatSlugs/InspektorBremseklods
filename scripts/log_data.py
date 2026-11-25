import cv 
from kamera import tag_bilede
from detect_shape import find_klodser

img = tag_bilede()
klods = find_klodser(img)

for x, y, vinkel in find_klodser:
    print(x, y , vinkel)
    cv.imshow ("data", img)
    cv. waitkey(0)
