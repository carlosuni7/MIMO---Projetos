console.log("Hello word!, My name is TypeScript")

let nome:string = "Carlos";
let idade:number = 23;
let ativo:boolean = true;

let nomeAdulto = "carlos"

function soma(a:string, b:number){
    return a + b;
}

soma("10", 5)

function somaSe(a:number, b:number): number {
    return a + b
}

soma("10", 5)

let notas:number[] = [8, 9, 10]
let nomes:string[] = ["ana", "joao"]

console.log("===============")
function saudacao(a:string, b:string):string {
    return a[0] + " e " + b[1]
}
console.log("===============")

function saudacaoNome(nome:string):string {
    return `Olá, ${nome}`
}

saudacaoNome("CARLOS ALESSANDRO")


console.log("==============")
let amigos:string = saudacao(nomes[0], nomes[1])
console.log(amigos)

const dobro = (n:number): number => n * 2;
console.log(dobro)

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