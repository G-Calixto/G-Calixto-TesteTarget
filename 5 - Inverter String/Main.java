import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Escreva a string que deseja inverter:  ");
    String frase = sc.nextLine();
    int tam = frase.length();
    for(tam--; tam>=0; tam--){
        System.out.printf("%c", frase.charAt(tam));

    }
    
    sc.close();
    }

}   
