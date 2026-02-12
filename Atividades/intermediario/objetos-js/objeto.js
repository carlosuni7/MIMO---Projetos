let arrayDevs = []

// No JavaScript, a variável de um objeto não guarda o objeto em si, mas sim o "endereço" dele na memória 

// Passagem por VALOR (Primitivos)
let meuLevel = 50;
let levelDoAmigo = meuLevel; // Copiou o valor 50

levelDoAmigo = 55; // Alterou a cópia

console.log(meuLevel) // Saida: 50 (A variavel original não mudou)
console.log(levelDoAmigo) // Saida: 55 (Alteramos apenas a cópia)
 console.log("======")
// Passagem por REFERÊNCIA (Objetos)
let meuDev = { nome: "Carlos", level: 90};
let devCompanheiro = meuDev; // Copiou a REFERÊNCIA (a "chave da casa");

devCompanheiro.level = 99; // Alterou o objeto original através da referência.

console.log(meuDev.level); // O original mudou
console.log(devCompanheiro.level) // Saida: 99 // Variavel que armazena a refencia do objeto

// NOTAÇÃO POR COLCHETES
// Usamos a notação por colchetes quando o nome da propriedade contem espaço, hifens etc...

// Propriedade com nome invalido

let relatorio = {
    "data de criação" : "2024-07-26",
    "id-do-usuario" : "abc-123"
};

console.log(relatorio["data de criação"])

// Bora ADICIONAR ALTERAR E REMOVER PROPRIEDADES

// 1. Adicionando uma nova propriedade
devCompanheiro.cidade = "São Paulo";
console.log(devCompanheiro.cidade); // Saída: "São Paulo"

// 2. Alterando uma propriedade existente
devCompanheiro.level = 36;
console.log(devCompanheiro.level); // Saída: 36

// 3. Removendo uma propriedade
delete devCompanheiro.ativo;
console.log(devCompanheiro.ativo); // Saída: undefined

console.log(devCompanheiro);

// Criamos uma função construtora
// o this se refere ao objeto que está sendo criar
// Se o objeto chamar novoDev. o This é trocado por "novoDev"
// Esta função é um molde de fabrica para criar novos objetos de Devs

function Dev(nome, level, techs) {
    this.nome = nome;
    this.level = level;
    this.techs = techs;
}
// Agora vamos usar nosso molde para criar novos devs!
let devBrendo = new Dev("Brendo", 25, "Full-Obra");
let devPh = new Dev("Ph", 21, "Java-Pro");

console.log(devBrendo.nome); // Saida: Brando
console.log(devPh.techs); // Saida: Java-Pro

arrayDevs.push(devBrendo, devPh)
console.log(arrayDevs)

// Uma propriedade do objeto pode armazenar outro objeto. Se chama: Aninhamento
// Desenvolvendo um objeto mais completo.

let perfilDev = {
    nome: "Brendo",
    level: 58,
    contato: {
        email: "brendo@gmail.com",
        github: "brendo_s@gitbuh.com",
        linkDin: "brendo_s@linkdin.com" 
    },
    skills: {
        frontEnd: ["HTML", "CSS", "React"],
        backEnd: ["Java", "Python"],
        mobile: ["React Native"]
    }
} // Um objeto completasso

// Para acessar as propriedades aninhadas encadeamos a notação de ponto
console.log(perfilDev.contato.email);
console.log(perfilDev.skills.frontEnd);
