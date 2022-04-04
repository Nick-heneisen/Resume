import java.util.Scanner;

public class E66 {
    public static void main(String[] args) {
        DataSet set = new DataSet();
        Scanner input = new Scanner(System.in);

        System.out.println("Input a number:");
        double num1 = input.nextDouble();
        set.add(num1);

        System.out.println("Input another number:");
        double num2 = input.nextDouble();
        set.add(num2);

        System.out.println("Input a final number:");
        double num3 = input.nextDouble();
        set.add(num3);

        System.out.println("Average is " + set.getAverage());
        System.out.println("Range is " + set.getRange());
        System.out.println("Smallest is " + set.getSmallest());
        System.out.println("Largest is " + set.getLargest());
    }
}
