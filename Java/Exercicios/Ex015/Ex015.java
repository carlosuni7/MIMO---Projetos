public class Ex015 {

    public static void main(String[] args) {
        
        int total = 0;

        for(int i = 0; i <= 1000; i++){
            if ((i % 2 == 0) && (i % 5 == 0) && (i % 7 == 0)) {
                System.out.println("Número: " + i );
                total += i;
            }
        }
        System.out.println("Somatória: " + total);
    }


}