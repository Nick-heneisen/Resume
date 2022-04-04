public class R114 {
    public static void main(String[] args) {
        double money = 10000, mWithdrawal = 500;
        double interest = .005;
        double years = 0;

        while (money >= 500) {
            double tester = money;

            money = money + (money * interest); // adds interest
            money -= mWithdrawal;

            if (money >= tester) {
                System.out.println("Program would go on forever.");
                break;
            }
            years = years + (1.0 / 12.0); // adds one month
        }
        System.out.println(years + " years.");
    }
}