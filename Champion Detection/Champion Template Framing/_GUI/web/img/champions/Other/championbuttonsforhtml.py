import eel
import io
import os
champions = os.listdir("..")

print(champions)

for champ in champions:
    print("<button onclick=\"toggleChamp('"+champ+"')\"><img id= '"+champ+"' src=\"img/champions/"+champ+"\"></button>")
