import java.util.Scanner;

public class P65 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter value to check primes to:");
        int value = input.nextInt();
        if (value >= 2) {
            System.out.println("2");
        }
        for (int i = 1; i < value; i++) {
            int prime = 0;
            int num = 0;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    prime = 1;
                    break;
                } else if (j == i - 1) {
                    num = i;
                }
            }
            if (prime < 1 && num != 0) {
                System.out.println(num);
            }
        }
    }
}
