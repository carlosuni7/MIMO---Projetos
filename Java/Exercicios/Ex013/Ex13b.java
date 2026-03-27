import javax.swing.JOptionPane;

public class Ex13b {

    public static void main(String[] args) {

        String Sexo = JOptionPane.showInputDialog(null,
                "Sexo (F - Feminino / M - Masculino");

        // ENTRADA DE DADOS EM  STRING
        // String strAltura = JOptionPane.showInputDialog(null,
        //         "Informe a sua altura: ");

        float Altura = Float.parseFloat(JOptionPane.showInputDialog("Informe uma Altura"));
            // Declarando variavel
        float PesoIdeal = 0.0f;

        Sexo.toUpperCase();

        if (Sexo.charAt(0) == 'F'){
            PesoIdeal = 62.1f * Altura - 44.7f;
        } else {
            PesoIdeal = 72.f * Altura - 58.0f;
        }

        JOptionPane.showMessageDialog(null, "Seu peso ideal é " + PesoIdeal);


    }
}