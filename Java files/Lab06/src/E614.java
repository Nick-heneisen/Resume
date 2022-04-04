import java.util.Scanner;

public class E614{
    public static void main (String[] args){
        Scanner input = new Scanner(System.in); // scans number
        System.out.println("Enter a number");
        int one = input.nextInt(); // takes number as a integer
        while (one != 0){ // if its not equal to 0 
            int answer = one % 2; // mod the asnwer  by 2
            System.out.println(answer);
            one = one / 2; // divide by 2
        }
    }
}