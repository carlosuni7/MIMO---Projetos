const reveals = document.querySelectorAll('.reveal');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('active');
      // se quiser que só revele uma vez:
    //   observer.unobserve(entry.target);
    }
    // se quiser remover active quando sai da viewport, comente a linha acima
     else entry.target.classList.remove('active');
  });
}, {
  root: null,           // viewport
  rootMargin: '0px 0px -10% 0px', // inicia um pouco antes de entrar totalmente
  threshold: 0.1        // quando 10% estiver visível
});

reveals.forEach(r => observer.observe(r));
