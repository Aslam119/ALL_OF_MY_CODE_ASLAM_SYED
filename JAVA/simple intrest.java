import java.text.NumberFormat;
import java.util.Scanner;

public class basic {
    public static void main(String[] args) {

    //PRINCIPAL
        System.out.print("Principal: ");
        Scanner Principal = new Scanner(System.in);
        int principal = Principal.nextInt();
    //RATE
        System.out.print("Annual Interest Rate: ");
        Scanner Rate = new Scanner(System.in);
        float rate = Rate.nextFloat();
    //TIME
        System.out.print("Period (Years): ");
        Scanner Time = new Scanner(System.in);
        int time = Time.nextInt();
    //CALCULATING SIMPLE INTEREST
        float simple = (principal*rate*time)/100;
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        System.out.println("Simple Intrest: "+ currency.format(simple));

    }
}


