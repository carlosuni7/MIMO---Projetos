let slides = document.querySelectorAll(".slide")

const proximoBtn = document.querySelector(".proximo");

const anteriorBtn = document.querySelector(".anterior");

proximoBtn.addEventListener('click', ()=>{
    slides.forEach((slide, index)=>{
        let slideAtivo = document.querySelector(".slide.active");
        slideAtivo.classList.remove("active")
        slides[index].classList.add("active");
    })
})