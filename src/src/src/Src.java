package src;

import java.util.Scanner;

public class Src{
    public static void main(String[] args){
        // TODO code application logic here
        int number;
        int number2;
        int aux = 0;
        Scanner teclado = new Scanner (System.in);
        
        System.out.println("Enter a number");
        number = teclado.nextInt();
        
        System.out.println("Enter a other number");
        number2 = teclado.nextInt();
        
        if (aux >= 100){
            aux = number - number2;
            
            System.out.println("Se produce la ley");
            System.out.println(aux);
        }
        else{
            aux = number - number2;
            
            System.out.println("No se produce la ley");
            System.out.println(aux);
        }
    }
}