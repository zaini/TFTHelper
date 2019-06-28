import eel

#ownedItems = ["bf_sword.png", "needlessly.png", "recurve_bow.png"]
#ownedItems = [0, 1, 2]

itemDictionary = {"bf_sword.png" : 0, "needlessly.png" : 1, "recurve_bow.png" : 2, "tear.png" : 3, "chain_vest.png" : 4, "negatron_cloak.png" : 5, "giants_belt.png" : 6, "golden_spatula.png" : 7}

reverseItemDictionary = {v: k for k, v in itemDictionary.items()}

#print(itemDictionary, reverseItemDictionary)

cheatsheet = [['infinity_edge.png', 'gunblade.png', 'divine.png', 'shojin.png', 'guardian_angel.png', 'bloodthirster.png', 'zekes_herald.png', 'ghostblade.png'],
              ['gunblade.png', 'rabadons.png', 'rageblade.png', 'ludens_echo.png', 'locket.png', 'ionic_spark.png', 'morellonomicon.png', 'yuumi.png'],
              ['divine.png', 'rageblade.png', 'firecannon.png', 'statikk_shiv.png', 'phantom_dancer.png', 'cursed_blade.png', 'titanic_hydra.png', 'botrk.png'],
              ['shojin.png', 'ludens_echo.png', 'statikk_shiv.png', 'seraphs.png', 'frozen_heart.png', 'hush.png', 'redemption.png', 'darkin.png'],
              ['guardian_angel.png', 'locket.png', 'phantom_dancer.png', 'frozen_heart.png', 'thornmail.png', 'sword_breaker.png', 'red_buff.png', 'knights_vow.png'],
              ['bloodthirster.png', 'ionic_spark.png', 'cursed_blade.png', 'hush.png', 'sword_breaker.png', 'dragons_claw.png', 'zephyr.png', 'runaans_hurricane.png'],
              ['zekes_herald.png', 'morellonomicon.png', 'titanic_hydra.png', 'redemption.png', 'red_buff.png', 'zephyr.png', 'warmogs.png', 'frozen_mallet.png'],
              ['ghostblade.png', 'yuumi.png', 'botrk.png', 'darkin.png', 'knights_vow.png', 'runaans_hurricane.png', 'frozen_mallet.png', 'force_of_nature.png']
              ]

#cheatsheetDictionary = {'infinity_edge.png' : 'Infinity Edge: Critical Strikes deal +100% damage', 'gunblade.png', : 'Hextech Gunblade: Heal for 25% of all damage dealt', 'divine.png', : 'Divine Sword: Each second: 5% change to only Critical Strike', 'shojin.png', : 'Spear of Shojin: After spell cast: Attacks give 20% of max Mana', 'guardian_angel.png', : 'Guardian Angel: Wearer gets revived with 300 HP (one time)', 'bloodthirster.png', : 'Bloodthirster: attacks heal for 50% of damage', 'zekes_herald.png', : 'Zeke\'s Herald: Adjacent allies gain +10% AS', 'ghostblade.png', : 'Youmuu\'s Ghostblade: Wearer is also an Assasin', 'rabadons.png', : 'Rabadon\'s Deathcap: +50% AP Hextech Gunblade: Heal for 25% of all damage dealt', 'rageblade.png', : 'Guinsoo\'s Rageblade: Attaks grant 3% AS (stacks infinitely)', 'ludens_echo.png', : 'Luden\'s Echo: Spells deal 100 splash damage on hit', 'locket.png', : 'Locket of the Solari: Adjacent allies gain a shield of 200 HP', 'ionic_spark.png', : 'Ionic Spark: Enimies take 100 damage after casting a spell', 'morellonomicon.png', : 'Morellonomicon: Spells apply burn: 10% of enemies max HP/s', 'yuumi.png', : 'Wearer is also a Sorcerer', 'firecannon.png', : 'Rapid Fire Cannon: Attacks cannot be dodged. 2x Attack Range', 'statikk_shiv.png', : 'Statikk Shiv: Every 3rd attack deals 100 splash damage', 'phantom_dancer.png', : 'Phantom Dancer: Wearer dodges all critical strikes', 'cursed_blade.png', : 'Cursed Blade: Attacks have a small change to Shrink (-1*)', 'titanic_hydra.png', : 'Titanic Hydra: Atttacks deal 10% of wearer's max HP as splash damage', 'botrk.png', : 'Blade of the Ruined King: Wearer is also Blademaster', 'seraphs.png', : 'Seraph\'s Embrace: Gain 20 Mana each time a spell is cast', 'frozen_heart.png', : 'Frozen Heart: Adjacent enemies lose 20% AS', 'hush.png', : 'Hush: Attacks have a high chance to Silence', 'redemption.png', : 'Redemption: On death: Heal all nearby allies for 1000 HP', 'darkin.png', : 'Wearer is also a Demon', 'thornmail.png', : 'Thornmail: Reflect 25% of damage from attacks', 'sword_breaker.png', : 'Sword Breaker: Attacks have a chance to Disarm', 'red_buff.png', : 'Red Buff: Attacks deal 10% burn damage', 'knights_vow.png', : 'Knight\'s Vow: Wearer is also a Knight', 'dragons_claw.png', : 'Dragon\'s Claw: Gain 83% resistance to magic damage', 'zephyr.png', : 'Zephyr: On start of combat: Banish an enemy for 5s', 'runaans_hurricane.png', : 'Runaan's Hurricane: Attack 2 extra targets with 50% of damage', 'warmogs.png', : 'Warmog\'s Armor: Regenerate 2.5% of max HP/s', 'frozen_mallet.png', : 'Frozen Mallet: Wearer is also Glacial', 'force_of_nature.png' : 'Force of Nature: Gain +1 team size'}

eel.init('web')

@eel.expose
def resetSelections():
    global ownedItems
    global ownedItemsNumbers
    global possibleItems
    
    ownedItems = []
    ownedItemsNumbers = []
    possibleItems = []
    
resetSelections()

@eel.expose
def addItem(item):
    ownedItems.append(item)
    ownedItemsNumbers.append(itemDictionary[item])
    return ownedItems

@eel.expose
def removeItem(item):
    ownedItems.remove(item)
    ownedItemsNumbers.remove(itemDictionary[item])
    return ownedItems

@eel.expose
def resultantItems(ownedItems):
    possibleItems = []
    if ownedItems == []:
        return possibleItems
    
    for a in ownedItemsNumbers:
        for b in ownedItemsNumbers:
            if cheatsheet[a][b] not in possibleItems:
                possibleItems.append(cheatsheet[a][b])

    return possibleItems

eel.start('index.html', size=(1920/1.4, 1080/1.4))
