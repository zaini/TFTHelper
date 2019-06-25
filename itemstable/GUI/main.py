import eel
import io

#ownedItems = ["bf_sword.png", "needlessly.png", "recurve_bow.png"]
ownedItems = [0, 1, 2]

itemDictionary = {"bf_sword.png" : 0, "needlessly.png" : 1, "recurve_bow.png" : 2, "tear.png" : 3, "chain_vest.png" : 4, "negatron_cloak.png" : 5, "giants_belt.png" : 6, "golden_spatula.png" : 7}

"""
cheatsheet = [['bf_sword.png', 'needlessly.png', 'recurve_bow.png', 'tear.png', 'chain_vest.png', 'negatron_cloak.png', 'giants_belt.png', 'golden_spatula.png'],
              ['bf_sword.png', 'infinity_edge.png', 'gunblade.png', 'divine.png', 'shojin.png', 'guardian_angel.png', 'bloodthirster.png', 'zekes_herald.png', 'ghostbalde.png'],
              ['needlessly.png', 'gunblade.png', 'rabadons.png', 'rageblade.png', 'ludens_echo.png', 'locket.png', 'ionic_spark.png', 'morellonomicon.png', 'yuumi.png'],
              ['recurve_bow.png', 'divine.png', 'rageblade.png', 'firecannon.png', 'statikk_shiv.png', 'phantom_dancer.png', 'cursed_blade.png', 'titanic_hydra.png', 'botrk.png'],
              ['tear.png', 'shojin.png', 'ludens_echo.png', 'statikk_shiv.png', 'seraphs.png', 'frozen_heart.png', 'hush.png', 'redemption.png', 'darkin.png'],
              ['chain_vest.png', 'guardian_angel.png', 'locket.png', 'phantom_dancer.png', 'frozen_heart.png', 'thornmail.png', 'sword_breaker.png', 'red_buff.png', 'knights_vow.png'],
              ['negatron_cloak.png', 'bloodthirster.png', 'ionic_spark.png', 'cursed_blade.png', 'hush.png', 'sword_breaker.png', 'dragons_claw.png', 'zephyr.png', 'runaans_hurricane.png'],
              ['giants_belt.png', 'zekes_herald.png', 'morellonomicon.png', 'titanic_hydra.png', 'redemption.png', 'red_buff.png', 'zephyr.png', 'warmogs.png', 'frozen_mallet.png'],
              ['golden_spatula.png', 'ghostblade.png', 'yuumi.png', 'botrk.png', 'darkin.png', 'knights_vow.png', 'runaans_hurricane.png', 'frozen_mallet.png', 'force_of_nature.png']
              ]
"""

cheatsheet = [['infinity_edge.png', 'gunblade.png', 'divine.png', 'shojin.png', 'guardian_angel.png', 'bloodthirster.png', 'zekes_herald.png', 'ghostbalde.png'],
              ['gunblade.png', 'rabadons.png', 'rageblade.png', 'ludens_echo.png', 'locket.png', 'ionic_spark.png', 'morellonomicon.png', 'yuumi.png'],
              ['divine.png', 'rageblade.png', 'firecannon.png', 'statikk_shiv.png', 'phantom_dancer.png', 'cursed_blade.png', 'titanic_hydra.png', 'botrk.png'],
              ['shojin.png', 'ludens_echo.png', 'statikk_shiv.png', 'seraphs.png', 'frozen_heart.png', 'hush.png', 'redemption.png', 'darkin.png'],
              ['guardian_angel.png', 'locket.png', 'phantom_dancer.png', 'frozen_heart.png', 'thornmail.png', 'sword_breaker.png', 'red_buff.png', 'knights_vow.png'],
              ['bloodthirster.png', 'ionic_spark.png', 'cursed_blade.png', 'hush.png', 'sword_breaker.png', 'dragons_claw.png', 'zephyr.png', 'runaans_hurricane.png'],
              ['zekes_herald.png', 'morellonomicon.png', 'titanic_hydra.png', 'redemption.png', 'red_buff.png', 'zephyr.png', 'warmogs.png', 'frozen_mallet.png'],
              ['ghostblade.png', 'yuumi.png', 'botrk.png', 'darkin.png', 'knights_vow.png', 'runaans_hurricane.png', 'frozen_mallet.png', 'force_of_nature.png']
              ]

eel.init('web')

@eel.expose
def resetSelections():
    global possibleItems
    global ownedItems
    
    ownedItems = []

    possibleItems = []
    
resetSelections()

@eel.expose
def addItem(item):
    if item in itemDictionary:
        ownedItems.append(itemDictionary[item])
    return ownedItems

@eel.expose
def resultantItems(ownedItems):
    for a in ownedItems:
        for b in ownedItems:
            if cheatsheet[a][b] not in possibleItems:
                possibleItems.append(cheatsheet[a][b])
    return possibleItems

eel.start('index.html', size=(1280, 720))
