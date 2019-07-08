import cv2
import numpy as np
from collections import Counter
from PIL import ImageGrab
import os
import time

def screenGrab():
    sc = ImageGrab.grab()
    #Names the screenshots and saves them in the specified folder
    screenshotname = "screenshot"+str(int(time.time()))+".png"
    sc.save(os.getcwd() + "\\livescreenshots\\" +screenshotname , "PNG")
    print(screenshotname)
    return screenshotname

#Stores the names of all the screenshots in the folder
filenames = os.listdir("screenshots")

#Gets the names of all the champions from the folder which has all the champion screenshots
#This can be changed so that it only looks for the champions you care for
champions = os.listdir("champions")
#GUI should add and remove champions from the following list
champions = ["darius.png", "garen.png", "vayne.png", "lucian.png"]

mode = input("A) use screenshots folder and output put results in championtest\nB) use live screenshots, save them in livescreenshots and output results in livechampiontest\n")

if mode.upper() == "A":
    for screenshot_name in filenames:
        #List where the current champions on screen are stored
        availablechampions = []

        #currentimg is the current screenshot being examined
        currentimg = cv2.imread("screenshots\\"+screenshot_name)

        #getting the resolution of the current image so that we can resize the champions icons
        w_screenshot, h_screenshot = currentimg.shape[:-1]

        #Resizing the champion icons, numbers here could be adjusted
        w = round(w_screenshot/(1080/185))
        h = round(h_screenshot/(1920/139))

        #Here is where each champion is to searched for in the current screenshot being examined
        for champion in champions:
            #resizing the champion icon
            query = cv2.resize(cv2.imread("champions/"+champion), (w, h))
            #show the resized champion icons
            #cv2.imshow('resized query', query)

            result = cv2.matchTemplate(currentimg, query, cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where(result >= threshold)

            #labelling the champion icons which have been detected and adding the found champions to the list
            for pt in zip(*loc[::-1]):
                cv2.rectangle(currentimg, pt, (pt[0] + w, pt[1] + h),(0,255,255),2)
                #print("found", x)
                availablechampions.append(champion)

        #Making a copy of the current screenshot but adding text and labelling it with what has been found
        currentimgwithtext = currentimg
        #cv2.putText(currentimgwithtext, str(Counter(availablechampions)), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(currentimgwithtext, str(list(set(availablechampions))), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

        #output the screenshots with text and labels on them
        #cv2.namedWindow('currentimgwithtext',cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('currentimgwithtext', round(1920/1.5),round(1080/1.5))
        #cv2.imshow("currentimgwithtext",currentimgwithtext)
        #cv2.waitKey(0)
        #cv2.destroyWindow("currentimgwithtext")

        #save labelled screenshots
        cv2.imwrite("championtest\\new"+screenshot_name, currentimgwithtext)
        
        #print(Counter(availablechampions))
        #print(list(set(availablechampions)))
        
        if availablechampions:
            print(list(set(availablechampions)))
            print("Found a champion you were looking for.")

if mode.upper() == "B":
    while True:
        #List where the current champions on screen are stored
        availablechampions = []

        #currentimg is the current screenshot being examined
        screenshot_name = screenGrab()
        currentScreen = cv2.imread("livescreenshots\\"+screenshot_name)

        #getting the resolution of the current image so that we can resize the champions icons
        w_screenshot, h_screenshot = currentScreen.shape[:-1]

        #Resizing the champion icons, numbers here could be adjusted
        w = round(w_screenshot/(1080/185))
        h = round(h_screenshot/(1920/139))

        #Here is where each champion is to searched for in the current screenshot being examined
        for champion in champions:
            #resizing the champion icon
            query = cv2.resize(cv2.imread("champions/"+champion), (w, h))
            #show the resized champion icons
            #cv2.imshow('resized query', query)

            result = cv2.matchTemplate(currentScreen, query, cv2.TM_CCOEFF_NORMED)
            threshold = 0.95
            loc = np.where(result >= threshold)

            #labelling the champion icons which have been detected and adding the found champions to the list
            for pt in zip(*loc[::-1]):
                cv2.rectangle(currentScreen, pt, (pt[0] + w, pt[1] + h),(0,255,255),2)
                #print("found", x)
                availablechampions.append(champion)

        #Making a copy of the current screenshot but adding text and labelling it with what has been found
        currentimgwithtext = currentScreen
        #cv2.putText(currentimgwithtext, str(Counter(availablechampions)), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(currentimgwithtext, str(list(set(availablechampions))), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

        #output the screenshots with text and labels on them
        #cv2.namedWindow('currentimgwithtext',cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('currentimgwithtext', round(1920/1.5),round(1080/1.5))
        #cv2.imshow("currentimgwithtext",currentimgwithtext)
        #cv2.waitKey(0)
        #cv2.destroyWindow("currentimgwithtext")

        #save labelled screenshots
        cv2.imwrite("livechampiontest\\new"+screenshot_name, currentimgwithtext)
        
        #print(Counter(availablechampions))
        #print(list(set(availablechampions)))
        
        if availablechampions: #checking if list is empty
            print(list(set(availablechampions)))
            print("Found a champion you were looking for.")
            #GUI should make a proper notfication from this


"""
no longer care about how many of each champ
if champ is found hten we want ot outpu t a noise to the user so they can react
user can select the champions they want to year a respond about
"""
