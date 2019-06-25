function showList(availableChampionsList) {
	//Use this to show to the user what they have selected if you wanna do that later on
	/**
	document.getElementById("listoutput").innerHTML = "python list:", availableChampionsList;
	document.getElementById("test").innerHTML = "length of lists:", availableChampionsListCopy.length;
	//return availableChampionsList
	copyavailableChampionsList = availableChampionsList
	**/
}

var copyownedItems = [];

//Made my Kamal
function updateSheet(item) {
	console.log(document.getElementById(item).src);
	//console.log(copyownedItems);

    if((document.getElementById(item).src == "http://localhost:8000/img/items/"+item)) {
        document.getElementById(item).src = "img/items/grayscale/gray"+item;
        //copyownedItems.push(item)

    }else if((document.getElementById(item).src == "http://localhost:8000/img/items/grayscale/gray"+item)) {
        document.getElementById(item).src = "img/items/"+item;
        //copyownedItems.splice(copyownedItems.indexOf(item), 1);
	//console.log(copyownedItems);

    }

}

function resetSelection(){
	eel.resetSelections()();
	eel.resultantItems([])(possibleItems);
	//console.log(copyownedItems);
	for (var i = copyownedItems.length - 1; i >= 0; i--) {
		console.log(copyownedItems[i]);
	}
	//console.log(copyownedItems);
	//document.getElementById(selections).innerHTML = ;
}

function selectItem(item){
	eel.addItem(item)(resultantItems);
	updateSheet(item);
	
}

function resultantItems(ownedItems){
	eel.resultantItems(ownedItems)(possibleItems);
	copyownedItems = ownedItems;

}

function possibleItems(x){
	document.getElementById('selection').innerHTML = x;

}