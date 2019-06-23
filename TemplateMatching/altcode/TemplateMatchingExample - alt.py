import cv2
import numpy as np

img_rgb = cv2.imread('screenshot.jpg')
template = cv2.imread('guinsoo.png')
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  # Switch collumns and rows
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow('result.png', img_rgb)

#https://stackoverflow.com/questions/7853628/how-do-i-find-an-image-contained-within-an-image
