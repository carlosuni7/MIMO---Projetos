function sendPost(){
    const texto = document.getElementById("result");
    const post = document.getElementById("sendText").value;
    texto.innerHTML = post;
}

function changeLayout () {
    const el = document.querySelector("img")
    el.style.display = "block";
}