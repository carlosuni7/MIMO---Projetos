const btnInicio = document.getElementById("inicio");
const btnFim = document.getElementById("fim");
const box = document.getElementById("container")
const range = document.getElementById("tamanho")
const valor = document.getElementById("valor")

btnInicio.addEventListener("click", () => {
    box.classList.remove("row-reverse")
})
btnFim.addEventListener("click", () => {
    box.classList.add("row-reverse")
})

range.addEventListener("input", () => {
    box.style.width = range.value + "px";
    valor.textContent = range.value;
})