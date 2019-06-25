import eel
import io

"""
button with picture of each champion.
pressing button adds and removes that champion from the list.
when the champion is found, play a sound
"""

champions = []

eel.init('web')

@eel.expose
def toggleChamp(champ):
    if champ in champions:
        champions.remove(champ)
        
    else:
        champions.append(champ)

@eel.expose
def printlist():
    print(champions)
    return champions

eel.start('index.html', size=(1280, 720))
