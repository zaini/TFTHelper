var ownedItems = [];
var possibleItems = [];
var ownedItemsNumbers = [];
var cheatsheetDictionary = {'infinity_edge.png' : 'Infinity Edge: Critical Strikes deal +100% damage', 'gunblade.png' : 'Hextech Gunblade: Heal for 25% of all damage dealt', 'divine.png' : 'Divine Sword: Each second: 5% change to only Critical Strike', 'shojin.png' : 'Spear of Shojin: After spell cast: Attacks give 20% of max Mana', 'guardian_angel.png' : 'Guardian Angel: Wearer gets revived with 300 HP (one time)', 'bloodthirster.png' : 'Bloodthirster: attacks heal for 50% of damage', 'zekes_herald.png' : 'Zekes Herald: Adjacent allies gain +10% AS', 'ghostblade.png' : 'Youmuus Ghostblade: Wearer is also an Assasin', 'rabadons.png' : 'Rabadons Deathcap: +50% AP Hextech Gunblade: Heal for 25% of all damage dealt', 'rageblade.png' : 'Guinsoos Rageblade: Attaks grant 3% AS (stacks infinitely)', 'ludens_echo.png'  : 'Ludens Echo: Spells deal 100 splash damage on hit', 'locket.png'  : 'Locket of the Solari: Adjacent allies gain a shield of 200 HP', 'ionic_spark.png'  : 'Ionic Spark: Enimies take 100 damage after casting a spell', 'morellonomicon.png'  : 'Morellonomicon: Spells apply burn: 10% of enemies max HP/s', 'yuumi.png'  : 'Wearer is also a Sorcerer', 'firecannon.png'  : 'Rapid Fire Cannon: Attacks cannot be dodged. 2x Attack Range', 'statikk_shiv.png'  : 'Statikk Shiv: Every 3rd attack deals 100 splash damage', 'phantom_dancer.png'  : 'Phantom Dancer: Wearer dodges all critical strikes', 'cursed_blade.png'  : 'Cursed Blade: Attacks have a small change to Shrink (-1*)', 'titanic_hydra.png'  : 'Titanic Hydra: Atttacks deal 10% of wearers max HP as splash damage', 'botrk.png'  : 'Blade of the Ruined King: Wearer is also Blademaster', 'seraphs.png'  : 'Seraphs Embrace: Gain 20 Mana each time a spell is cast', 'frozen_heart.png'  : 'Frozen Heart: Adjacent enemies lose 20% AS', 'hush.png'  : 'Hush: Attacks have a high chance to Silence', 'redemption.png'  : 'Redemption: On death: Heal all nearby allies for 1000 HP', 'darkin.png'  : 'Wearer is also a Demon', 'thornmail.png' : 'Thornmail: Reflect 25% of damage from attacks', 'sword_breaker.png' : 'Sword Breaker: Attacks have a chance to Disarm', 'red_buff.png' : 'Red Buff: Attacks deal 10% burn damage', 'knights_vow.png' : 'Knights Vow: Wearer is also a Knight', 'dragons_claw.png' : 'Dragons Claw: Gain 83% resistance to magic damage', 'zephyr.png' : 'Zephyr: On start of combat: Banish an enemy for 5s', 'runaans_hurricane.png' : 'Runaans Hurricane: Attack 2 extra targets with 50% of damage', 'warmogs.png' : 'Warmogs Armor: Regenerate 2.5% of max HP/s', 'frozen_mallet.png' : 'Frozen Mallet: Wearer is also Glacial', 'force_of_nature.png' : 'Force of Nature: Gain +1 team size'};
var itemDictionary = {"bf_sword.png" : 0, "needlessly.png" : 1, "recurve_bow.png" : 2, "tear.png" : 3, "chain_vest.png" : 4, "negatron_cloak.png" : 5, "giants_belt.png" : 6, "golden_spatula.png" : 7};
var cheatsheet = [['infinity_edge.png', 'gunblade.png', 'divine.png', 'shojin.png', 'guardian_angel.png', 'bloodthirster.png', 'zekes_herald.png', 'ghostblade.png'],
              ['gunblade.png', 'rabadons.png', 'rageblade.png', 'ludens_echo.png', 'locket.png', 'ionic_spark.png', 'morellonomicon.png', 'yuumi.png'],
              ['divine.png', 'rageblade.png', 'firecannon.png', 'statikk_shiv.png', 'phantom_dancer.png', 'cursed_blade.png', 'titanic_hydra.png', 'botrk.png'],
              ['shojin.png', 'ludens_echo.png', 'statikk_shiv.png', 'seraphs.png', 'frozen_heart.png', 'hush.png', 'redemption.png', 'darkin.png'],
              ['guardian_angel.png', 'locket.png', 'phantom_dancer.png', 'frozen_heart.png', 'thornmail.png', 'sword_breaker.png', 'red_buff.png', 'knights_vow.png'],
              ['bloodthirster.png', 'ionic_spark.png', 'cursed_blade.png', 'hush.png', 'sword_breaker.png', 'dragons_claw.png', 'zephyr.png', 'runaans_hurricane.png'],
              ['zekes_herald.png', 'morellonomicon.png', 'titanic_hydra.png', 'redemption.png', 'red_buff.png', 'zephyr.png', 'warmogs.png', 'frozen_mallet.png'],
              ['ghostblade.png', 'yuumi.png', 'botrk.png', 'darkin.png', 'knights_vow.png', 'runaans_hurricane.png', 'frozen_mallet.png', 'force_of_nature.png']
              ];


//Inverts the item colour
function updateSheet(item, colour) {
	var imageSourceForItem = document.getElementsByClassName(item);
	if(item.includes("2")){
		item = item.slice(0,-1);
	}

	if(colour == null){
		for (var i = imageSourceForItem.length - 1; i >= 0; i--) {
			if(imageSourceForItem[i].src.includes("img/items/"+item)) {
	       		imageSourceForItem[i].src = "img/items/grayscale/gray"+item;

	  		}else if(imageSourceForItem[i].src.includes("img/items/grayscale/gray"+item)) {
	        	imageSourceForItem[i].src = "img/items/"+item;

	   		};

		};
	}else if (colour == true) {
		for (var i = imageSourceForItem.length - 1; i >= 0; i--) {
			if(imageSourceForItem[i].src.includes("img/items/grayscale/gray"+item)) {
	        	imageSourceForItem[i].src = "img/items/"+item;
	        };
		};
	}else if (colour == false) {
		for (var i = imageSourceForItem.length - 1; i >= 0; i--) {
			if(imageSourceForItem[i].src.includes("img/items/"+item)) {
	       		imageSourceForItem[i].src = "img/items/grayscale/gray"+item;
	        };
		};
	};
};

function selectItem(item){
	//Only accept inputs if the item clicked is a primary item
	if(['bf_sword.png', 'needlessly.png', 'recurve_bow.png', 'tear.png', 'chain_vest.png', 'negatron_cloak.png', 'giants_belt.png', 'golden_spatula.png', 'bf_sword.png2', 'needlessly.png2', 'recurve_bow.png2', 'tear.png2', 'chain_vest.png2', 'negatron_cloak.png2', 'giants_belt.png2', 'golden_spatula.png2'].includes(item)){
		//if item is already in currently owned then we want to remove it, if not owned we want to add it and update everything
		if(ownedItems.includes(item)){
			ownedItemsNumbers.splice(ownedItems.indexOf(item), 1);
			ownedItems.splice(ownedItems.indexOf(item), 1);
			
		}else{
			ownedItems.push(item);
			if(item.includes("2")){
				ownedItemsNumbers.push(itemDictionary[item.slice(0, -1)]);

			}else{
				ownedItemsNumbers.push(itemDictionary[item]);
			}
			
		};

		//Clears all highlighted possible items
		for (var i = possibleItems.length - 1; i >= 0; i--) {
			updateSheet(possibleItems[i], false);

		};

		possibleItems = [];

		//If no items are owned then keep possibleItems empty. Otherwise we want to find what the possible items are before highlighting them
		if(ownedItems == []){
			//pass
		}else{
			for (var a = ownedItemsNumbers.length - 1; a >= 0; a--) {
				for (var b = ownedItemsNumbers.length - 1; b >= 0; b--) {
					if (possibleItems.includes(cheatsheet[ownedItemsNumbers[a]][ownedItemsNumbers[b]]) == false && a != b) {
						possibleItems.push(cheatsheet[ownedItemsNumbers[a]][ownedItemsNumbers[b]]);
						//console.log("possible items:"+possibleItems)

					};
				};
			};

		};

		//Highlight the possibleItems
		for (var i = possibleItems.length - 1; i >= 0; i--) {
			updateSheet(possibleItems[i], true);
			
		};

		addItemToCraftable(possibleItems);

		//Updates the sheet for the selected items
		updateSheet(item, null);

	}

}

function resetSelection(){
	//Update table so that primary and secondary items are gray and ownedItems, ownedItemsNumbers and possibleItems lists are empty. Then call addItemToCraftable to clear that too.
	for (var i = ownedItems.length - 1; i >= 0; i--) {
		updateSheet(ownedItems[i], false);
	};
	ownedItems = [];
	ownedItemsNumbers = [];

	for (var i = possibleItems.length - 1; i >= 0; i--) {
		updateSheet(possibleItems[i], false);
	};

	possibleItems = [];
	
	//console.log(possibleItems, ownedItems, ownedItemsNumbers);

	addItemToCraftable(possibleItems);

}

function addItemToCraftable(possibleItems){
	//imageSourceForItem is a list for each slot
	var imageSourceForItem = document.getElementsByClassName('item');

	//Clear the Craftable items table then fill it with possibleitems
	for (var i = imageSourceForItem.length - 1; i >= 0; i--) {
		imageSourceForItem[i].innerHTML = "<td class = 'item' style='width: 64px; height: 64px;'></td>";

	};
	for (var i = possibleItems.length - 1; i >= 0; i--) {
		imageSourceForItem[i].innerHTML = "<td class = 'item'><div class='tooltip'><img class= '"+possibleItems[i]+"' src='img/items/"+possibleItems[i]+"'><span class='tooltiptext'>"+cheatsheetDictionary[possibleItems[i]]+"</span></div></td>";
		possibleItems[i];

	};

}

//Tab Functionality
function openTab(evt, tabName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}