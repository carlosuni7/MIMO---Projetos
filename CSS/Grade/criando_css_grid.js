const flexbtn = document.getElementById("flex");
const gridbtn = document.getElementById("grid")
const container = document.getElementById("container");
const itens = document.querySelectorAll(".item");
const titulo = document.getElementById("titulo");

flexbtn.addEventListener('click', () => {
    container.classList.remove("grid-container");
    container.classList.add("flex-container");
    titulo.textContent = "One Dimensions"
})

gridbtn.addEventListener('click', () => {
    container.classList.add("grid-container");
    container.classList.remove("flex-container");
    titulo.textContent = "Two Dimensions"
})