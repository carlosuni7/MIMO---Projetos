let beverage = ['Chá', 'Café', 'Limonada', 'Agua', 'Suco de laranja', 'Refrigerante', 'Vinho', 'Cerveja'];

function escolhaUmaBebidaAleatoria() {
    return new Promise((resolve, reject) => {
        let indiceAleatorio = Math.floor(Math.random() * beverage.length);
        let bebidaSelecionada = beverage[indiceAleatorio];
        
        setTimeout(function(){
            console.log(`${bebidaSelecionada} foi selecionada`);
            resolve(bebidaSelecionada);
        }, 1000);
    });
}

function verifcaSeAguaEstaPronta(isbebidaSelecionada) {
    return new Promise((resolve, reject) => {
        setTimeout(function(){
            if(isbebidaSelecionada){
               resolve(console.log('Preparando...'));
            } else {
                reject("Nenhuma bebida foi retirada..");
            }
        }, 1000)
    });
}

function prepararBebida(bebidaSelecionada) {
    return new Promise((resolve, reject) =>{
        setTimeout(function(){
            if(bebidaSelecionada){
                
                resolve(console.log(`Aproveite o seu  ${bebidaSelecionada} !`));
            } else {
                reject("A bebida ainda não está pronta...");
            }
        }, 1000)
    })
}

async function tratamentoPromessasNativas(){
    const bebidaEscolhida = await escolhaUmaBebidaAleatoria();
    const aguaQuentePronta = await verifcaSeAguaEstaPronta(bebidaEscolhida);
    const bebidaPreparada = await prepararBebida(bebidaEscolhida);
    return bebidaPreparada;
}

tratamentoPromessasNativas();