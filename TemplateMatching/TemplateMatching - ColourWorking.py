import cv2
import numpy as np
mainimage = "screenshot.jpg"
img = cv2.imread(mainimage)
#img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

queryimage = "guinsoo" #these names need to follow the standard uses in the cheatsheet, ideally turned into numbers
query = cv2.imread("items/"+queryimage+".jpg")

w, h = query.shape[:-1]
#w, h = query.shape[::-1]

result = cv2.matchTemplate(img, query, cv2.TM_CCOEFF_NORMED)
threshold = 0.83
loc = np.where(result >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h),(0,255,255),2)

cv2.imshow('detected', img)
cv2.waitKey(0)
cv2.destroyWindow("detected")
