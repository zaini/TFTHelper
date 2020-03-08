import eel
import io
import cv2
import numpy as np
from PIL import ImageGrab
import os
import time

"""
button with picture of each champion.
pressing button adds and removes that champion from the list.
when the champion is found, play a sound

use js to edit list
then send list to python to check screenshot, if champion is on screen
then output sound
"""

eel.init('web')

#print(os.listdir("champions"))
#Champions we are looking for in screenshots
#champions = ["darius.png", "garen.png", "vayne.png", "lucian.png"]

def screenGrab():
    sc = ImageGrab.grab()
    screenshotname = "screenshot"+str(int(time.time()))+".png"
    sc.save(os.getcwd() + "\\livescreenshots\\" +screenshotname , "PNG")
    return screenshotname

@eel.expose
def checkCurrentScreen(champions):
    print(champions)
    onScreenChampions = [] #No champions found on screen yet

    screenshot_name = screenGrab() #Get name of screenshot and read it into cv2 as currentScreen
    currentScreen = cv2.imread("livescreenshots\\"+screenshot_name)

    w_screenshot, h_screenshot = currentScreen.shape[:-1] #Get dimensions of screenshot

    #Define the dimensions we want the champion icons to be, based on the dimensions of the screenshot
    w = round(w_screenshot/(1080/185))
    h = round(h_screenshot/(1920/139))

    #Where each champion is checked
    for champion in champions:
        query = cv2.resize(cv2.imread("../champions/"+champion), (w, h)) #Resizes the champion icon accordingly and reads it into the variable query

        result = cv2.matchTemplate(currentScreen, query, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = np.where(result >= threshold)

        #Labels currentScreen where champion is found, prints which champion is found and adds them to the list of champions on the screen
        for pt in zip(*loc[::-1]):
            cv2.rectangle(currentScreen, pt, (pt[0] + w, pt[1] + h),(0,255,255),2)
            onScreenChampions.append(champion)
            print("Found", champion)

    if onScreenChampions: #If something is on screen, print the list
        print(list(set(onScreenChampions)))
        eel.playSound()
        #If this is running, user should be notified

    eel.runCheckScreen(champions)
    #checkCurrentScreen(champions)

eel.start('index.html', size=(1280, 720))
print("started")
