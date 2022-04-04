import java.util.Scanner;

public class P62 {
    public static void main(String[] args) {
        Boolean entering = true;
        DataSet set = new DataSet();
        Scanner input = new Scanner(System.in);
        while (entering) {
            System.out.println("Input a number to enter or a letter to find average / SD:");
            if (input.hasNextDouble()) {
                double num = input.nextDouble();
                set.add(num);
            } else {
                System.out.println("Average is " + set.getAverage());
                System.out.println("Standard Deviation is: " + set.getStandardDeviation());
                entering = false;
            }

        }
    }
}
   