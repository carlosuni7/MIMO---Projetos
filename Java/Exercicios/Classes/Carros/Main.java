public class Main {
    public static void main(String[] args) {
        Carro newCarro;
        newCarro = new Carro();
        
        System.out.println("O carro " + newCarro.nome + " segue o modelo: " + newCarro.modelo + " criado em " + newCarro.anoFabricacao + " pela " + newCarro.marca);
        newCarro.speed(236);
        System.out.println(newCarro);
        
    }
}
