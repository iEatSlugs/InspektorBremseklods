import cv2 as cv
import numpy as np 
from roi import klip_roi,  y_start, x_start, linjer_roi

areal = 10000
grænse = 170


def srt_hvid(img):
    roi = klip_roi(img)
    gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (5, 5), 0)
    _, bw = cv.threshold(gray, grænse, 255, cv.THRESH_BINARY_INV)
    kerne = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    bw = cv.morphologyEx(bw, cv.MORPH_OPEN, kerne)
    return bw

def find_centrum(kontur):
    M = cv.moments(kontur)
    x = int(M["m10"] / M["m00"])
    y = int(M["m01"] / M["m00"])
    return x, y

def find_klodser(img):
    bw = srt_hvid(img)
    konturer, _ = cv.findContours(bw, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE,
                                  offset=(x_start, y_start))

    klodser = []
    for kontur in konturer:
        if cv.contourArea(kontur) < areal:
            continue

        x, y = find_centrum(kontur)
        klodser.append((kontur, x, y))

    return klodser


def tegn_klods(img, kontur, x, y, vinkel):
    cv.drawContours(img, [kontur], 0, (0, 255, 0), 2)
    cv.circle(img, (x, y), 6, (0, 0, 255), -1)
    tekst = f"x={x} y={y} {vinkel:.0f}"
    cv.putText(img, tekst, (x - 80, y - 15), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    klodser = []

    return klodser

if __name__ == "__main__":
    img = cv.imread(r"c:\Users\PC User\Pictures\testbilleder\billede_20.jpg")

    linjer_roi(img)
    for kontur, x, y in find_klodser(img):
        tegn_klods(img, kontur, x, y, 0)

    cv.imshow("orale",img)
    cv.waitKey(0)
    cv.destroyAllWindows()