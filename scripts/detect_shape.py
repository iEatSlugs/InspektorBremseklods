import cv2 as cv
import numpy as np 


def find_klodser(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (5, 5), 0)
    h, w = gray.shape

    bw = cv.adaptivethreshhold (gray, 255, cv.adaptivethreshhold(gray,255, cv.adaptive_thresh_mean_c, cv.thresh_binary_inv, 101,10))
    bw = cv.morphologyex(bw, cv.morph_close, cv.getstructuringelement(cv.MORPH_ELLIPSE, (5,5)))
    bw = cv.morphologyex(bw, cv.morph_close, cv.getstructuringelement(cv.MORPH_ELLIPSE, (15, 15)))
    konturer, _ = cv.findContours(bw, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    klodser = []
    for klods in konturer:
        x, y, w, h = cv.boundingRect(klods)
        if cv.contourArea(klods) < 20000 or x < 10 or y < 10 or x + w > w - 10 or y + h > h - 10:
            continue

        approx = cv.approxPolyDP(klods, 0.005 * cv.arcLength(klods, True), True)

        (cx, cy), (b, l), vinkel = cv.minAreaRect(klods)
        if b < l:
            vinkel += 90
        vinkel %= 180

        
        klodser.append((cx, cy, vinkel))

        cv.drawContours(img, [approx], 0, (0, 255, 0), 2)
        cv.circle(img, (int(cx), int(cy)), 8, (0, 0, 255), -1)
        cv.putText(img, f"X={cx:.0f} Y={cy:.0f} {vinkel:.0f} grader", (int(cx) - 120, int(cy) - 20),
                    cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    return klodser
if __name__ == "__main__": img = cv.imread("bremsklods1.jpg") 
klodser = find_klodser(img)
print(klodser)
cv.imshow("Klodser", img)
cv.waitKey(0)
cv.destroyAllWindows()