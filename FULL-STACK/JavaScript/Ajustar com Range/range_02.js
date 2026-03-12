const range = document.getElementById('volume');
const valor = document.getElementById('valor');

// Atualiza o número conforme o usuário move o slider
range.addEventListener('input', () => {
  valor.textContent = range.value;
});
