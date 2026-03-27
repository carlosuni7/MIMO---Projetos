public class Principal {
    
    public static void main(String[] args) {
        
        //  Criar um objeto da minha classe (Instanciar)
        Retangulo ret = new Retangulo(2, 5);
        
        System.out.println("Valor da base = " + ret.getBase());
        System.out.println("Valor da altura = " + ret.getAltura());
        System.out.println("Area = " + ret.CalcularArea());
        System.out.println("Perimetro = " + ret.CalcularPerimetro());

        
    }


}
