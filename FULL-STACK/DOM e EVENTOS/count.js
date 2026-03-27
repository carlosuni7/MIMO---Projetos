


let textarea = document.getElementById("mensagem");
let count = document.getElementById("count")

let conteudo = textarea.value;

textarea.addEventListener("input", function(){
    console.log(`Digitando... ${this.value}`)
    qtd = textarea.value.length
    count.innerHTML = qtd
})

console.log("-------")


// function exibeText(){
//     let textarea = document.getElementById("mensagem");
//     let count = document.getElementById("count")

//     let conteudo = textarea.value;

//     console.log(conteudo)
//     count.textContent = conteudo
// }

exibeText();

