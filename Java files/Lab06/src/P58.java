import java.util.Scanner;

public class P58 {
    public static void main(String[] args) {
        System.out.println("is leap year? " + isLeapYear());
    }
    public static boolean isLeapYear() {
        Scanner yearScanner = new Scanner(System.in);
        System.out.println("Enter year:");
        String year = yearScanner.nextLine();
        int yearInt = Integer.parseInt(year);
        if (yearInt % 4 == 0) {
            return yearInt % 100 != 0 || yearInt % 400 == 0;
        } else {
            return false;
        }
    }
}
