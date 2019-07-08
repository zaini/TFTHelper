var currentownedItems = [];
var activepossibleItems = [];
var cheatsheetDictionary = {'infinity_edge.png' : 'Infinity Edge: Critical Strikes deal +100% damage', 'gunblade.png' : 'Hextech Gunblade: Heal for 25% of all damage dealt', 'divine.png' : 'Divine Sword: Each second: 5% change to only Critical Strike', 'shojin.png' : 'Spear of Shojin: After spell cast: Attacks give 20% of max Mana', 'guardian_angel.png' : 'Guardian Angel: Wearer gets revived with 300 HP (one time)', 'bloodthirster.png' : 'Bloodthirster: attacks heal for 50% of damage', 'zekes_herald.png' : 'Zekes Herald: Adjacent allies gain +10% AS', 'ghostblade.png' : 'Youmuus Ghostblade: Wearer is also an Assasin', 'rabadons.png' : 'Rabadons Deathcap: +50% AP Hextech Gunblade: Heal for 25% of all damage dealt', 'rageblade.png' : 'Guinsoos Rageblade: Attaks grant 3% AS (stacks infinitely)', 'ludens_echo.png'  : 'Ludens Echo: Spells deal 100 splash damage on hit', 'locket.png'  : 'Locket of the Solari: Adjacent allies gain a shield of 200 HP', 'ionic_spark.png'  : 'Ionic Spark: Enimies take 100 damage after casting a spell', 'morellonomicon.png'  : 'Morellonomicon: Spells apply burn: 10% of enemies max HP/s', 'yuumi.png'  : 'Wearer is also a Sorcerer', 'firecannon.png'  : 'Rapid Fire Cannon: Attacks cannot be dodged. 2x Attack Range', 'statikk_shiv.png'  : 'Statikk Shiv: Every 3rd attack deals 100 splash damage', 'phantom_dancer.png'  : 'Phantom Dancer: Wearer dodges all critical strikes', 'cursed_blade.png'  : 'Cursed Blade: Attacks have a small change to Shrink (-1*)', 'titanic_hydra.png'  : 'Titanic Hydra: Atttacks deal 10% of wearers max HP as splash damage', 'botrk.png'  : 'Blade of the Ruined King: Wearer is also Blademaster', 'seraphs.png'  : 'Seraphs Embrace: Gain 20 Mana each time a spell is cast', 'frozen_heart.png'  : 'Frozen Heart: Adjacent enemies lose 20% AS', 'hush.png'  : 'Hush: Attacks have a high chance to Silence', 'redemption.png'  : 'Redemption: On death: Heal all nearby allies for 1000 HP', 'darkin.png'  : 'Wearer is also a Demon', 'thornmail.png' : 'Thornmail: Reflect 25% of damage from attacks', 'sword_breaker.png' : 'Sword Breaker: Attacks have a chance to Disarm', 'red_buff.png' : 'Red Buff: Attacks deal 10% burn damage', 'knights_vow.png' : 'Knights Vow: Wearer is also a Knight', 'dragons_claw.png' : 'Dragons Claw: Gain 83% resistance to magic damage', 'zephyr.png' : 'Zephyr: On start of combat: Banish an enemy for 5s', 'runaans_hurricane.png' : 'Runaans Hurricane: Attack 2 extra targets with 50% of damage', 'warmogs.png' : 'Warmogs Armor: Regenerate 2.5% of max HP/s', 'frozen_mallet.png' : 'Frozen Mallet: Wearer is also Glacial', 'force_of_nature.png' : 'Force of Nature: Gain +1 team size'};

//Inverts the item colour
function updateSheet(item, colour) {
	var imageSourceForItem = document.getElementsByClassName(item);

	if(colour == null){
		for (var i = imageSourceForItem.length - 1; i >= 0; i--) {
			if((imageSourceForItem[i].src == "http://localhost:8000/img/items/"+item)) {
	       		imageSourceForItem[i].src = "img/items/grayscale/gray"+item;

	  		}else if((imageSourceForItem[i].src == "http://localhost:8000/img/items/grayscale/gray"+item)) {
	        	imageSourceForItem[i].src = "img/items/"+item;

	   		};

		};
	}else if (colour == true) {
		for (var i = imageSourceForItem.length - 1; i >= 0; i--) {
			if((imageSourceForItem[i].src == "http://localhost:8000/img/items/grayscale/gray"+item)) {
	        	imageSourceForItem[i].src = "img/items/"+item;
	        };
		};
	}else if (colour == false) {
		for (var i = imageSourceForItem.length - 1; i >= 0; i--) {
			if((imageSourceForItem[i].src == "http://localhost:8000/img/items/"+item)) {
	       		imageSourceForItem[i].src = "img/items/grayscale/gray"+item;
	        };
		};
	};
};

function selectItem(item){
	if(['bf_sword.png', 'needlessly.png', 'recurve_bow.png', 'tear.png', 'chain_vest.png', 'negatron_cloak.png', 'giants_belt.png', 'golden_spatula.png'].includes(item)){
		//if item is already in currently owned then we want to remove it and update everything if it's not then we want to add it and update
		if(currentownedItems.includes(item)){
			eel.removeItem(item)(resultantItems);

		}else{
			eel.addItem(item)(resultantItems);

		};

		//Updates the sheet for the selected items
		updateSheet(item, null);

	}

}

function updateResultantItems(colour){
	console.log("activepossibleItems");
	for (var i = activepossibleItems.length - 1; i >= 0; i--) {
		updateSheet(activepossibleItems[i], colour);

	};
	
};

function resultantItems(ownedItems){
	//clear whole board and then highlight the currentpossibleitems
	currentownedItems = ownedItems;
	//clearing board

	for (var i = activepossibleItems.length - 1; i >= 0; i--) {
		updateSheet(activepossibleItems[i], false);
	};

	eel.resultantItems(ownedItems)(function(possibleItems){
		activepossibleItems = possibleItems;
		//possibleItems is the items we have so we want them to be coloured
		for (var i = possibleItems.length - 1; i >= 0; i--) {
			updateSheet(possibleItems[i], true)
		};
		console.log(activepossibleItems);
		addItemToCraftable(activepossibleItems);
	});


}

function resetSelection(){
	console.log(activepossibleItems, currentownedItems);
	eel.resetSelections()();

	for (var i = currentownedItems.length - 1; i >= 0; i--) {
		updateSheet(currentownedItems[i], false);
	};
	currentownedItems = [];

	for (var i = activepossibleItems.length - 1; i >= 0; i--) {
		updateSheet(activepossibleItems[i], false);
	};
	activepossibleItems = [];

	addItemToCraftable(activepossibleItems);

}

function addItemToCraftable(activepossibleItems){
	//imageSourceForItem is a list for each slot
	var imageSourceForItem = document.getElementsByClassName('item');

	//Clear the Craftable items table then fill it with possibleitems
	for (var i = imageSourceForItem.length - 1; i >= 0; i--) {
		imageSourceForItem[i].innerHTML = "<td class = 'item' style='width: 64px; height: 64px;'></td>";

	};


	for (var i = activepossibleItems.length - 1; i >= 0; i--) {
		imageSourceForItem[i].innerHTML = "<td class = 'item'><div class='tooltip'><img class= '"+activepossibleItems[i]+"' src='img/items/"+activepossibleItems[i]+"'><span class='tooltiptext'>"+cheatsheetDictionary[activepossibleItems[i]]+"</span></div></td>";
		activepossibleItems[i];

	};

}
