// O .style é um objeto, não uma função. Então você não usa parênteses () — usa atribuição (=).

const btnColuna = document.getElementById("btn-column");
const colunaReverse = document.getElementById("btn-columnReverse");
const btnLinha = document.getElementById("btn-row");
const linhaReverse = document.getElementById("btn-rowReverse")
const container = document.getElementById("container");

btnColuna.addEventListener('click', () => {
    // container.classList.add("div-column")
    // container.classList.remove("div-row")
    container.style.flexDirection = "column";
})

btnLinha.addEventListener('click', () => {
    // container.classList.remove("div-column")
    // container.classList.add("div-row")
    container.style.flexDirection = "row";
})
linhaReverse.addEventListener('click', () => {
    container.style.flexDirection = "row-reverse";

})
colunaReverse.addEventListener('click', () => {
    container.style.flexDirection = "column-reverse";
})