import java.text.DecimalFormat;

public class Ex011 {
    public static void main(String[] args) {
        

        final float PRECO_CUSTO = 37.00f;

        float PercentVendedor = PRECO_CUSTO * 0.12f;
        float PercentImposto = PRECO_CUSTO * 0.2695f;
        float valorProduto = PRECO_CUSTO + PercentVendedor + PercentImposto;

        // DecimalFormat é uma forma de você formatar numeros float para exibir em tela 
        DecimalFormat df = new DecimalFormat("0.00");
        //  Resultado formatado
        String resultado = df.format(valorProduto);

        System.err.println("Valor do Produto com Porcentagem do Vendedor: R$ " + resultado);



    }
}
