var currentownedItems = [];
var activepossibleItems = [];

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

}

