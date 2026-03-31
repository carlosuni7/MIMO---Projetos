"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var nome = "Carlos";
var idade = 23;
var ativo = true;
var nomeAdulto = "carlos";
function viraString(a, b) {
    return a + b;
}
var resul = viraString("10", 5);
console.log(resul);
function somaNumber(a, b) {
    return Number(a) + b;
}
console.log(somaNumber(15, 26));
var notas = [8, 9, 10];
var nomes = ["ana", "joao"];
function saudacao(a, b) {
    return a + " e " + b;
}
;
function meuNome(nome) {
    return "Ol\u00E1, ".concat(nome);
}
meuNome("CARLOS ALESSANDRO");
console.log("==============");
var amigos = saudacao(nomes[0], nomes[1]);
console.log(amigos);
var dobro = function (n) { return n * 2; };
console.log(dobro(5));
var user = {
    nome: "Carlos",
    idade: 22,
    ativo: true
};
console.log(user);
