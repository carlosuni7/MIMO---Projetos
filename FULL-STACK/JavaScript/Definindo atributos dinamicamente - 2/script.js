
function mudarEstilo() {
    const parag = document.querySelector("p");
    const container = document.querySelector("div");
    container.innerHTML = parag.style.color;
}

function changeColor () {
    const el = document.querySelector("p");
    el.style.color = "#d7465f";
}

function mudarBackground () {
    const el = document.querySelector("p");
    el.style.backgroundColor = "#d7465f";
    el.style.color = "white";
    el.style.padding = "10px";
}