import cv2
import os
champions = os.listdir("..")

print(champions)

for champ in champions:
    if champ != "Other":
        image = cv2.imread("..\\"+champ, 0)
        cv2.imwrite("gray"+champ, image)
