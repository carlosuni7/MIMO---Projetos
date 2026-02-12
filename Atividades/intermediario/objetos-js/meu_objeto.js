const devProfile = {
    nome : "Carlos",
    apelido : "Carlinhos",
    level : 8,
    techs : ["JavaScript", "React", "Gsap", "PHP"],
    ativo : true,
    // declaracao : escrevePessoa(perfilDev)
}

// Objetos incluindo arrays são passados por referência

let perfilDev = devProfile; // Copiou a REFERÊNCIA (a "chave da casa")

function displayObjeto (objeto) {
    let nomePessoa = objeto.nome;
    let nivel = objeto.level;
    let tecnologia = objeto.techs;

    const descri = `Meu nome: ${nomePessoa} meu nivel ${nivel}, minhas techs ${tecnologia} `
    return descri
}

const exibir = displayObjeto(perfilDev);
console.log(exibir);

console.log(perfilDev)
// 1 - Adicionando uma nova propriedade
perfilDev.cidade = "Sud Mennucci";
console.log(perfilDev.cidade)

// 2 - Alterando propriedade
perfilDev.level = 23;
console.log(perfilDev.level)

// 3 _ Removendo uma propriedade
delete perfilDev.ativo;
console.log(perfilDev.ativo)

// console.log(perfilDev.nome) // Saida "carlos"

// perfilDev.nome = "Alessandro" // Alterei o objeto original
// console.log(perfilDev.nome) // Saide: "Alessandro"
// console.log(devProfile); // O atributo nome atualiza pra: "Alessandro";
