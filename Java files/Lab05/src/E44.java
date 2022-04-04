import java.util.Scanner;
import java.lang.Math;

public class E44 {
    public static void main(String args[]){
        Scanner ousman=new Scanner(System.in);
        System.out.println("enter two numbers, separated by a space: ");
        int one=ousman.nextInt(); //first integer
        int two=ousman.nextInt(); //second integer

        System.out.println("sum: "+sum(one, two));
        System.out.println("difference: "+difference(one, two));
        System.out.println("product: "+product(one, two));
        System.out.println("average: "+average(one, two));
        System.out.println("distance: "+distance(one, two));
        System.out.println("maximum value: "+maximum(one, two));
        System.out.println("minimum value: "+minimum(one, two));
    }
    public static int sum(int one, int two){
        return one+two;
    }
    public static int difference(int one, int two){
        return one-two;
    }
    public static int product(int one, int two){
        return one*two;
    }
    public static int average(int one, int two){
        return sum(one, two)/2; //jack's drippy answer
        //return (one+two)/2
    }
    public static int distance(int one, int two){
//        int x=difference(one, two); go teddy!!!!!!!!
//        if(x<0){
//            return -1*x;
//        }
//        else{
//            return x;
//        }
        return Math.abs(one-two);
    }
    public static int maximum(int one, int two){
        return Math.max(one, two);
    }
    public static int minimum(int one, int two){
        return Math.min(one, two);
    }
}