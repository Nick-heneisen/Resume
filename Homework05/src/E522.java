import java.util.Scanner;

public class E522 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter a floating-point number: ");
        double number1 = input.nextDouble();  // Read user input
        System.out.println(number1);

        System.out.println("Enter another floating-point number: ");
        double number2 = input.nextDouble();  // Read user input
        System.out.println(number2);

        number1 = number1 * 100;
        number1 = Math.floor(number1);
        number1 = number1 / 100;

        number2 = number2 * 100;
        number2 = Math.floor(number2);
        number2 = number2 / 100;

        if (number1 == number2) {
            System.out.print("They are the same up to two decimal places.");
        } else {
            System.out.print("They are different.");
        }
    }
}
