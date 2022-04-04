import java.util.Scanner;

public class P63{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your number:");
        int fold = input.nextInt();
        int fold1 = 0;
        int fold2 = 1;
        int foldNew = 0;
        int count = 0;
        for (count = 0; count < fold; count++){
            foldNew = fold1 + fold2;
            fold2 = fold1;
            fold1 = foldNew;
        }
        System.out.print("the " + count +"th Fibonacci is " + foldNew);
    }
}