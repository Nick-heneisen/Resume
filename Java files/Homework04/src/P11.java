public class P11 {
    public static void main(String[] args) {
        double ticketPrice = 10; // dollars
        double gasPricePG = 4; // price per gallon
        double maintenance = .05; // cents per mile
        double efficiency = 1; // miles per gallon
        double distance = 20; // in miles

        double carPrice = (maintenance * distance) + (gasPricePG * (distance / efficiency));
        if (carPrice < ticketPrice) {
            System.out.println("Car is cheaper.");
            System.out.println("Car: $" + carPrice);
            System.out.println("Train: $" + ticketPrice);
        } else {
            System.out.println("Train is cheaper.");
            System.out.println("Car: $" + carPrice);
            System.out.println("Train: $" + ticketPrice);
        }
    }
}
