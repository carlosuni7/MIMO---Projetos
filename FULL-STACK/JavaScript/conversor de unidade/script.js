
      const selecionado = document.getElementById("selecao");
      const resultado = document.getElementById("resultado");
      const inputValor = document.getElementById("inputValor");
      const botao = document.getElementById("botao");

      const FATOR_CONVERSAO = 1.609;

      function converter() {
        const valor = Number(inputValor.value);
        const unidade = selecionado.value;

        if (!valor) {
          resultado.classList.add("erro")
          resultado.innerHTML = "Insira um valor válido";
          return
        }

        resultado.classList.remove("erro");

        let convertido;
        let unidadeFinal;

        if (unidade == "kilometro") {
          convertido = valor * FATOR_CONVERSAO;
          unidadeFinal = "Quilômetro";
        }

        else if (unidade == "milha") {
          convertido = valor / FATOR_CONVERSAO;
          unidadeFinal = "Milhas";
        }
        
        resultado.innerHTML = `Resultado: ${convertido.toFixed(3)} ${unidadeFinal}`;
      }

      console.log("vsdjnvdsvsd")

      botao.addEventListener("click", converter);