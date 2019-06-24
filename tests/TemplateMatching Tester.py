import cv2
import numpy as np
from collections import Counter
from PIL import ImageGrab
import os
import time

testname = "test1"

#filenames of all the screenshots taken during a game
filenames = os.listdir(r"C:\Users\Aros\Desktop\TFT App\TemplateMatching\tests\\"+testname+"\screenshots")

itemlist = ['bf_sword.png', 'bloodthirster.png', 'botrk.png', 'cursed_blade.png', 'darkin.png', 'divine.png', 'dragons_claw.png', 'firecannon.png', 'force_of_nature.png', 'frozen_heart.png', 'frozen_mallet.png', 'ghostblade.png', 'guardian_angel.png', 'gunblade.png', 'hush.png', 'infinity_edge.png', 'ionic_spark.png', 'knights_vow.png', 'locket.png', 'ludens_echo.png', 'morellonomicon.png', 'phantom_dancer.png', 'rabadons.png', 'rageblade.png', 'redemption.png', 'red_buff.png', 'runaans_hurricane.png', 'seraphs.png', 'shojin.png', 'statikk_shiv.png', 'sword_breaker.png', 'thornmail.png', 'titanic_hydra.png', 'warmogs.png', 'yuumi.png', 'zekes_herald.png', 'zephyr.png']
rawitemlist = ['chain_vest.png', 'giants_belt.png', 'golden_spatula.png', 'needlessly.png', 'negatron_cloak.png', 'recurve_bow.png', 'tear.png']
someitemslist = itemlist + rawitemlist

for file in filenames:
    itemsowned = []
    
    mainimage = testname+"\\screenshots\\"+file
    img = cv2.imread(mainimage)

    w_screenshot, h_screenshot = img.shape[:-1]

    w = round(w_screenshot/(1080/22))
    h = round(h_screenshot/(1920/22))
       
    for item in someitemslist:
        textimg = img
        queryimage = item
        query1 = cv2.imread("../items/"+queryimage)

        #w1/w = 1080/21  so we resize query for the screenshot 
        query = cv2.resize(query1, (w, h))
        #cv2.imshow('resized query', query)

        result = cv2.matchTemplate(textimg, query, cv2.TM_CCOEFF_NORMED)
        threshold = 0.72
        loc = np.where(result >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(textimg, pt, (pt[0] + w, pt[1] + h),(0,255,255),2)
            #print("found", x)
            itemsowned.append(item)
        # Write some Text
        
    textimg = img
    cv2.putText(textimg, str(Counter(itemsowned)), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

    #Display the image
    #cv2.namedWindow('textimg',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('textimg', round(1920/1.5),round(1080/1.5))
    #cv2.imshow("textimg",textimg)
    cv2.imwrite(testname+"\\testresults\\new"+file,textimg)
    #cv2.waitKey(10)
    #cv2.destroyWindow("textimg")

    #cv2.imshow('detected', img)
    #cv2.waitKey(0)
    #cv2.destroyWindow("detected")
    
    print(file, Counter(itemsowned))
    #time.sleep(3)
