class Livro {
  constructor(titulo, autor, paginas, lido = false) {
    this.titulo = titulo;
    this.autor = autor;
    this.paginas = paginas;
    this.lido = lido;
  }

  get status() {
    return this.lido ? "Lido" : "Não lido";
  }

  mararLido(lido = true){
    this.lido = lido;
  }

}

export { Livro };
