var copyownedItems = [];
var copypossibleItems = [];

function updateSheet(item) {
	var imageSourceForItem = document.getElementsByClassName(item);

	for (var i = imageSourceForItem.length - 1; i >= 0; i--) {
		if((imageSourceForItem[i].src == "http://localhost:8000/img/items/"+item)) {
       		imageSourceForItem[i].src = "img/items/grayscale/gray"+item;

  		}else if((imageSourceForItem[i].src == "http://localhost:8000/img/items/grayscale/gray"+item)) {
        	imageSourceForItem[i].src = "img/items/"+item;

   		}

	};

}

function selectItem(item){
	if(['bf_sword.png', 'needlessly.png', 'recurve_bow.png', 'tear.png', 'chain_vest.png', 'negatron_cloak.png', 'giants_belt.png', 'golden_spatula.png'].includes(item)){
		eel.addItem(item)(resultantItems);
		updateSheet(item);
	}

}

function resultantItems(ownedItems){
	eel.resultantItems(ownedItems)(possibleItems);
	copyownedItems = ownedItems;

}

function resetSelection(){
	eel.resetSelections()();
	eel.resultantItems([])(possibleItems);
	for (var i = copyownedItems.length - 1; i >= 0; i--) {
		updateSheet(copyownedItems[i]);
	};
	copyownedItems = [];

	for (var i = copypossibleItems.length - 1; i >= 0; i--) {
		updateSheet(copypossibleItems[i]);
	};
	copypossibleItems = [];
}

function possibleItems(possibleItemsList){
	//document.getElementById('selection').innerHTML = possibleItemsList;
	for (var i = possibleItemsList.length - 1; i >= 0; i--) {
		if(copypossibleItems.includes(possibleItemsList[i])){
			//pass
		}else{
			updateSheet(possibleItemsList[i])
			copypossibleItems.push(possibleItemsList[i])
		}
	};

}