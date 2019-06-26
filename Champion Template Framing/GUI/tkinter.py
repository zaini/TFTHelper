import cv2
import numpy as np
from collections import Counter
from PIL import ImageGrab
import os
import time
from tkinter import *
import threading
from queue import Queue

"""
button with picture of each champion.
pressing button adds and removes that champion from the list.
when the champion is found, play a sound
"""

#Gets the names of all the champions from the folder which has all the champion screenshots
#This can be changed so that it only looks for the champions you care for
champions = os.listdir("champions")

#GUI should add and remove champions from the following list
champions = ["darius.png", "garen.png", "vayne.png", "lucian.png"]


class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("TFT Helper")
        
        self.pack(fill=BOTH, expand = 1)
        
        #quitButton = Button(self, text="quit program", command = self.client_exit)
        #quitButton.place(x=0, y=0)

        vayneButton = Button(self, text="Toggle Vayne", command = self.toggleVayne)
        vayneButton.place(x=0, y=0)

        printButton = Button(self, text="Available Champs", command = self.printlist)
        printButton.place(x=100, y=0)

    def client_exit(self):
        exit()

    def toggleVayne(self):
        if "vayne.png" in champions:
            champions.remove("vayne.png")
            
        else:
            champions.append("vayne.png")

    def printlist(self):
        print(champions)
        
root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()

#print(champions)
