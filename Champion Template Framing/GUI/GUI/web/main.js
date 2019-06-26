var champions = [];

function showList(availableChampionsList) {
	//Use this to show to the user what they have selected if you wanna do that later on
	/**
	document.getElementById("listoutput").innerHTML = "python list:", availableChampionsList;
	document.getElementById("test").innerHTML = "length of lists:", availableChampionsListCopy.length;
	//return availableChampionsList
	copyavailableChampionsList = availableChampionsList
	**/
}

//Made my Kamal
function toggleChamp(champion) {
	console.log(document.getElementById(champion).src);
	eel.toggleChamp(champion);
    if((document.getElementById(champion).src == "http://localhost:8000/img/champions/"+champion)) {
        champions.push(champion);
        document.getElementById(champion).src = "img/champions/grayscale/gray"+champion;


    } else if((document.getElementById(champion).src == "http://localhost:8000/img/champions/grayscale/gray"+champion)) {
        champions.splice(champions.indexOf(champion), 1);
        document.getElementById(champion).src = "img/champions/"+champion;
    }

    eel.printlist()(showList);
}

var audio = new Audio('audio/lightsound.mp3');

function updateChamps(){
	audio.play();
}