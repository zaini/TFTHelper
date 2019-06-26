import cv2
import numpy as np
from collections import Counter
from PIL import ImageGrab
import os
import time

def screenGrab():
    sc = ImageGrab.grab()
    name = "screenshot"+str(int(time.time()))+".png"
    sc.save(os.getcwd() + "\\screenshots\\" +name , "PNG")
    print(name)
    return name

itemlist = ['bf_sword.png', 'bloodthirster.png', 'botrk.png', 'cursed_blade.png', 'darkin.png', 'divine.png', 'dragons_claw.png', 'firecannon.png', 'force_of_nature.png', 'frozen_heart.png', 'frozen_mallet.png', 'ghostblade.png', 'guardian_angel.png', 'gunblade.png', 'hush.png', 'infinity_edge.png', 'ionic_spark.png', 'knights_vow.png', 'locket.png', 'ludens_echo.png', 'morellonomicon.png', 'phantom_dancer.png', 'rabadons.png', 'rageblade.png', 'redemption.png', 'red_buff.png', 'runaans_hurricane.png', 'seraphs.png', 'shojin.png', 'statikk_shiv.png', 'sword_breaker.png', 'thornmail.png', 'titanic_hydra.png', 'warmogs.png', 'yuumi.png', 'zekes_herald.png', 'zephyr.png']
rawitemlist = ['chain_vest.png', 'giants_belt.png', 'golden_spatula.png', 'needlessly.png', 'negatron_cloak.png', 'recurve_bow.png', 'tear.png']
someitemslist = itemlist + rawitemlist

while True:
    itemsowned = []
    
    mainimage = "screenshots\\"+screenGrab()
    img = cv2.imread(mainimage)

    w_screenshot, h_screenshot = img.shape[:-1]

    w = round(w_screenshot/(1080/22))
    h = round(h_screenshot/(1920/22))
       
    for item in someitemslist:
        queryimage = item
        query1 = cv2.imread("items/"+queryimage)

        #w1/w = 1080/21  so we resize query for the screenshot 
        query = cv2.resize(query1, (w, h))
        #cv2.imshow('resized query', query)

        result = cv2.matchTemplate(img, query, cv2.TM_CCOEFF_NORMED)
        threshold = 0.72
        loc = np.where(result >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h),(0,255,255),2)
            #print("found", x)
            itemsowned.append(item)

        #cv2.imshow('detected', img)
        #cv2.waitKey(0)
        #cv2.destroyWindow("detected")

        img = cv2.imread(mainimage)
        

    print(Counter(itemsowned))
    #time.sleep(3)
