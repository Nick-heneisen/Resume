import java.util.Scanner;

public class P64 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter value to factor:");
        int value = input.nextInt();
        FactorGenerator numbers = new FactorGenerator(value);
        System.out.println("The Factors are:");
        while(numbers.hasMoreFactors()){
            System.out.println(numbers.nextFactor());
        }
    }
}