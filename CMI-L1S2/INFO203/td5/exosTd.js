function cliqueUn() {
	alert("vous venez de cliquer");
}

var compteur = 0;
function cliqueDeux() {
	compteur = compteur +1;
	alert("Vous avez cliqué "+compteur+ " fois");
}

function eurosVersDollards(valeurEuros) {
	dol = valeurEuros*1.2;
	alert(dol+" dollards");
}

function eurosVersDollards2(valeurEuros) {
	dollars.value=valeurEuros*1.2;
}

function proposition(nom,valeur) {
	document.getElementById("displayName").innerHTML = nom;
	document.getElementById("displayValue").innerHTML = valeur;
}

function toRed(){
	document.getElementById("tochange").backgroundColor = "red";
}
