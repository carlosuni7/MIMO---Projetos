
const botao = document.querySelectorAll('.btn');
let resultado = document.querySelector('.result');

botao.forEach(btn => {
    let texto = btn.textContent;
    btn.addEventListener('click', () => {
        if (texto === 'Marte') {
            resultado.classList.remove(".incorreto");
            resultado.classList.add("correto");
            resultado.innerHTML = 'Correto! Marte é conhecido como o Planeta Vermelho.';
        }


        if (texto !== 'Marte') {
            resultado.classList.remove("correto");
            resultado.classList.add("incorreto");
            resultado.innerHTML = 'Incorreto! Tente novamente.';
        }
    })
})

let respostas = ['Terra', 'Marte', 'Jupiter', 'Saturno'];
console.log(typeof respostas);

