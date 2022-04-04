import java.util.Scanner;

public class E419 {
    public static void main(String args[]){
        Scanner meredith=new Scanner(System.in);
        System.out.println("input a number corresponding to a month of the year: ");
        int wantMonth=meredith.nextInt();
        String months="January  February March    April    May      June     July     August   SeptemberOctober  November December ";
        System.out.println("the corresponding month is: "+months.substring((wantMonth-1)*9, ((wantMonth-1)*9)+9));
    }
}