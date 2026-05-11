// Se existir algo salvo carrega
// Se não existir nada, cria um arrays vazio
let arraysDev = JSON.parse(localStorage.getItem("devs")) || [];

// Essa função salvar no local storage do navegador o arrayDev
function salvarDev() {
    localStorage.setItem("devs", JSON.stringify(arraysDev))
}


let inNome = document.getElementById("inNome");
let inProfissao = document.getElementById("inProfissao");
let inTechs = document.getElementById("inTech");
let listadev = document.getElementById("listaDevs");
const listUl = document.getElementById("listUl");


const botaoForm = document.getElementById("btnForm");
const botaoExibir = document.getElementById("btnExibir")

botaoForm.addEventListener("click", () => {

    let innome = inNome.value;
    let inprofissao = inProfissao.value;
    let intechs = inTechs.value;

    let usuario = new Dev(innome, inprofissao, intechs);

    arraysDev.push(usuario);
    
    salvarDev();
    renderizarDev();
    
})

function Dev(nome, level, techs) {
    this.nome = nome,
        this.profissional = level,
        this.techs = techs
}

function renderizarDev() {
    listUl.innerHTML = ""

    arraysDev.forEach(dev => {
        const li = document.createElement("li");

        li.textContent = `
            Nome: ${dev.nome}, 
            Profissão: ${dev.profissional}, 
            Techs: ${dev.techs}
        `;

        listUl.appendChild(li);
    });
}

botaoExibir.addEventListener("click", renderizarDev)
console.log(arraysDev)






