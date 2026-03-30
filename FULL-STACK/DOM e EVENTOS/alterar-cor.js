let rangeRed = document.getElementById('rangeRed');
let rangeGreen = document.getElementById('rangeGreen');
let rangeBlue = document.getElementById('rangeBlue') ;
let resultado = document.getElementById('resultado');

let red = document.querySelector('.red')
let green = document.querySelector('.green')
let blue = document.querySelector('.blue')


function inputRGB(){

    let r = Number(rangeRed.value);
    let g = Number(rangeGreen.value);
    let b = Number(rangeBlue.value);

    red.textContent = r;
    green.textContent = g;
    blue.textContent = b;

    const valores = `rgb(${r}, ${g}, ${b})`;

    resultado.style.backgroundColor = valores;
    resultado.textContent = valores;

    if(r > 128 || g > 128 || b > 128){
        resultado.style.color = 'black';
    } else {
        resultado.style.color = 'white';
    };
}

inputRGB();

