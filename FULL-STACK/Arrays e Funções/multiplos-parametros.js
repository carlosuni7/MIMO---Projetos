
        let form = document.getElementById("form");
        let nome = document.getElementById("nome");
        let sobrenome = document.getElementById("sobrenome");
        const numberTeam = 3
        let arrayNome = []

        const botao = document.getElementById("button")

        function getName(primeiro, segundo){
            return `${primeiro} ${segundo}`
        }

        function addArray(nomecompleto){
            arrayNome.push(nomecompleto);

        }

        function team(completo){
            if(arrayNome.length < 3){
            let paragrafo = document.createElement("p")

            paragrafo.innerHTML = completo;
            form.appendChild(paragrafo)
            } else {
                paragrafo.textContent = "Sua equipe está cheia";
            }
        }

        botao.addEventListener("click", () =>{
            let nomeCompleto = getName(nome.value, sobrenome.value)

            addArray(nomeCompleto);

            console.log(arrayNome)

            team(nomeCompleto)
        })

        // botao.addEventListener("click", () => {
        //     let nomeCompleto = getName(nome.value, sobrenome.value);
        //     arrayNome.push(nomeCompleto)
            
        //     let texto = document.createElement("p");

        //     for(let i = 0; i < arrayNome.length; i++){

        //         if(arrayNome.length < 3 ){
        //             texto.innerHTML = arrayNome[i];
        //         }
        //         else {
        //             texto.innerHTML = "A equipe está cheia";
        //         }
                
        //         form.appendChild(texto);
        //     }
            
        //     console.log(arrayNome)
        // })
