
// Salvando no local storage
// Verifica se o array possui conteudo, se tiver carrega, se não cria um array vazio
// localStorage.getItem tenta pegar algo salvo com essa chave "personagens"
let personagens = JSON.parse(localStorage.getItem("personagens") || [])


// Definição da Classe com constra Maiuscula
class Personagem {
    // Construtor da classe onde construimos o objeto
    // com os dados passados e outras providencias
    constructor(nome, raca, poder){
        this.nome = nome,
        this.raca = raca,
        this.poder = poder
    }

    // Métodos são comportamentos do objeto.
    // Quando o objeto executa alguma ação
    imprimirDescricao() {
        return `
        Descrição: ${this.nome}, poder: ${poder}, raça: ${this.raca}
        `
    }
}

const goku = new Personagem("Goku", "Sayajin", "Kamehameha");
const vegeta = new Personagem("Vegetta", "Sayajin", "Galick Gun");
const picolo = new Personagem("Picollo", "Namekusenjin", "Makankosappo");
const gohan = new Personagem("Gohan","Sayajin", "Kamehameha");

console.log(goku);
console.log(vegeta);
console.log(picolo);
console.log(gohan);