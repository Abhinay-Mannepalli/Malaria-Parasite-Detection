import cv2

import pandas as pd
import csv

image = cv2.imread('1.jpg')


blur = cv2.blur(image,(5,5),5) # (9 x 9) filter is used 



gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


canny = cv2.Canny(image, 50, 200)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contours,0, (155,0,0), 3)

cv2.destroyAllWindows()
a=[0]
i=0
for i in range(10):
    try:
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if(area>0.0):
            a.append(area)
    except:
        a.append(0)
print(a)
cv2.imshow('rgb',canny)



