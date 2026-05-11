import { Livro } from "./classe_livro.js";

let biblioteca = [];

let livro1 = new Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1178, true);
let livro2 = new Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 223);
let livro3 = new Livro("O Código Da Vinci", "Dan Brown", 454);

livro1.mararLido(); // Alterando o status de leitura do livro1 para "Lido"
livro2.mararLido();
livro3.mararLido();

console.log(livro1);
biblioteca.push(livro1, livro2, livro3);

console.log(biblioteca);

document.body.innerHTML = `<h1>Minha Biblioteca</h1><br>`;

// const htmlContent = biblioteca
//   .map(
//     (livro) => `
//     <div class="livro">
//     <h2>${livro.titulo}</h2>
//     <p>Status: ${livro.status}</p>
//     </div>
//     `,
//   )
//   .join("");

document.body.innerHTML += biblioteca
  .map(
    (livro) => `
    <div class="livro">
    <h2>${livro.titulo}</h2>
    <p>Status: ${livro.status}</p>
    </div>`,
  )
  .join("<br>");
