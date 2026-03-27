public class Retangulo {

    // Definição do atributos da Classe
    private int Base, Altura;
    
    // Criação dos Métodos (Ações) => Funções

    // Método Construtor
    public Retangulo(int base, int altura) {
        Base = base;
        Altura = altura;
    }

    // Métodos Getter -> Recupear um valor de atributo
    // - Sempre retorna um valor do tipo correspondente 
    // ao seu atributo
    // - Não recebe nenhum parametro
    // - Somente retorna o valor do atributo correspondente
    public int getBase(){
        return Base;
    }

    public int getAltura(){
        return Altura;
    }


    // Métodos Setter -> Atribui um valor a uma propriedade
    // - Sempre é void <==> Nunca retorna valor
    // - Sempre recebe um parametro do tipo a qual
    //   corresponde seu atributo
    //  Somente realiza a atribuição do valor a sua propriedade
    public void setBase(int b){
        Base = b;
    }

    public void setAltura(int a){
        Altura = a;
    }

    public int CalcularArea(){
        return getBase() * getAltura();
    }

    public int CalcularPerimetro(){
        return (getBase() * 2 + getAltura() * 2);
    }

}
