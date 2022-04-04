import java.util.Scanner;

public class E417 {
    public static void main(String args[]){
        Scanner varoon=new Scanner(System.in);
        //23:14 = 11:14pm
        System.out.println("Enter the first time in military format (ex: 23:14=11:14pm): ");
        String firstNum=varoon.nextLine(); //first input
        System.out.println("Enter the second time in military format: ");
        String secNum=varoon.nextLine(); //second input

        int hour1=Integer.valueOf(firstNum.substring(0,2)); //inclusive on the first, exclusive on the second
        int min1=Integer.valueOf(firstNum.substring(3,5));
        int hour2=Integer.valueOf(secNum.substring(0,2)); //inclusive on the first, exclusive on the second
        int min2=Integer.valueOf(secNum.substring(3,5));

        int time1=hour1*60+min1; //total hours and minutes in minute unit
        int time2=hour2*60+min2;

        int difference=(time2-time1+1440)%1440; //1440=number of minutes in a day
        int hours=difference/60; //return back to hours format
        int minutes=difference%60; //return back to minutes format

        System.out.println("the difference between the times are: "+hours+" hours and "+minutes+" minutes.");
    }
}