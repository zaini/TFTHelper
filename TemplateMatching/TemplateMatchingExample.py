import cv2
import numpy as np
mainimage = "screenshot.jpg"
img_bgr = cv2.imread(mainimage)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

queryimage = "guinsoo.png"
query = cv2.imread(queryimage, 0)

w, h = query.shape[::-1]

result = cv2.matchTemplate(img_gray, query, cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where(result >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h),(0,255,255),2)

cv2.imshow('detected', img_bgr)
