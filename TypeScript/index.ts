export {};

let nome:string = "Carlos";
let idade:number = 23;
let ativo:boolean = true;

let nomeAdulto:string = "carlos";

function viraString (a:string, b:number){
    return a + b;
}

const resul:string = viraString("10", 5);
console.log(resul)

function somaNumber(a:number | string, b:number): number {
    return Number(a) + b;
}
console.log(somaNumber(15,26));

let notas:number[] = [8, 9, 10];
let nomes:string[] = ["ana", "joao"];


function saudacao (a:string, b:string):string {
    return a + " e " + b;
};



function meuNome (nome:string):string {
    return `Olá, ${nome}`;
}

meuNome("CARLOS ALESSANDRO")


console.log("==============")
let amigos:string = saudacao(nomes[0], nomes[1])
console.log(amigos)

const dobro = (n:number): number => n * 2;
console.log(dobro(5))

interface Usuario {
    nome: string
    idade: number
    ativo: boolean
}

const user: Usuario = {
    nome: "Carlos",
    idade: 22,
    ativo: true
}

console.log(user)