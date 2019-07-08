import numpy as np
import cv2
from PIL import ImageGrab
import time

import eel

eel.init('web')

screenshot = np.array(ImageGrab.grab())
w_screenshot, h_screenshot = screenshot.shape[:-1] #Get dimensions of screenshot

#Define the dimensions we want the champion icons to be, based on the dimensions of the screenshot
w = round(w_screenshot/(1080/185))
h = round(h_screenshot/(1920/139))

#champions = [["darius.png", cv2.resize(cv2.imread("champions/"+"darius.png"), (w, h))], ["garen.png", cv2.resize(cv2.imread("champions/"+"garen.png"), (w, h))]]

champions = []

@eel.expose
def championsReceiver(JSchampions):
    for champion in JSchampions:
        champions.append([champion, cv2.resize(cv2.imread("../champions/"+champion), (w, h))])
    #print(champions)
    
@eel.expose
def runNotifier():
    last_time = time.time()
    while True:
        screenshot = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_BGR2RGB)

        onScreenChampions = [] #No champions found on screen yet

        #Where each champion is checked
        for champion in champions:
            query = champion[1] #Resizes the champion icon accordingly and reads it into the variable query

            result = cv2.matchTemplate(screenshot, query, cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where(result >= threshold)

            #Labels currentScreen where champion is found, prints which champion is found and adds them to the list of champions on the screen
            for pt in zip(*loc[::-1]):
                cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h),(0,255,255),2)
                onScreenChampions.append(champion[0])
                print("Found", champion[0])

        if onScreenChampions: #If something is on screen, print the list
            print(list(set(onScreenChampions)))
            eel.playSound()
            #If this is running, user should be notified

        #eel.runCheckScreen(champions)
        #checkCurrentScreen(champions)
            
        print('Loop took {} seconds',format(time.time()-last_time))
        
        last_time = time.time()

    #eel.sendChampionsToPython([])

eel.start('index.html', size=(1280, 720))
