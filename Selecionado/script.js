function showSelection(){
const texto = document.getElementById("result");
const selectedColor = document.getElementById("colorSelect").value;
texto.innerHTML = "You picked: " + selectedColor;

}

function showCountry (){
    const texto = document.getElementById("resultC");
    const selectedCountry = document.getElementById("countrySelect").value;
    texto.innerHTML = "O pais selecionado: " + selectedCountry;
}

function showVolume () {
    const texto = document.getElementById("resultVol")
    const selectedVol = document.getElementById("volSelect").value;
    texto.innerHTML = "O volume está: " + selectedVol;
}

function selOptions() {
    const texto = document.getElementById("resultOp")
    const options = document.getElementById("options").value;
    texto.innerHTML = "Você escolheu a: " + options;
}

function search() {
    const selectedOp = document.getElementById("searchSelect").value;
    document.getElementById("message").innerHTML = selectedOp;
}