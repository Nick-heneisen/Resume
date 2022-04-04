import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Card {
    String descripSuit = null;
    String descripNum = null;

    public static void main(String[] args)  {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter card: ");
        String card = input.nextLine();
        String finalCard = card.substring(0, 1);
        String finalSuit = card.substring(1);
        Card myCard = new Card();
        System.out.println("Your card is: " + myCard.getDescription(finalCard, finalSuit));
    }

    public String getDescription(String number, String suit) {
        System.out.println(suit);
        System.out.println(number);
        List<String> faces = new ArrayList<>();
        faces.add("Q");
        faces.add("K");
        faces.add("J");
        faces.add("A");

        List<String> suits = new ArrayList<>();
        suits.add("S");
        suits.add("C");
        suits.add("H");
        suits.add("D");

        List<String> numbers = new ArrayList<>();;
        numbers.add("2");
        numbers.add("3");
        numbers.add("4");
        numbers.add("5");
        numbers.add("6");
        numbers.add("7");
        numbers.add("8");
        numbers.add("9");
        numbers.add("10");
        if (suits.contains(suit)) {
            if (suit.equals("S")) {
                descripSuit = "Spades";
            } else if (suit.equals("H")) {
                descripSuit = "Hearts";
            } else if (suit.equals("D")) {
                descripSuit = "Diamonds";
            } else if (suit.equals("C")) {
                descripSuit = "Clubs";
            } else {
                return "Unknown";
            }
        }
        if (numbers.contains(number)) {
            descripNum = number;
        } else if (faces.contains(number)) {
            if (number.equals("K")) {
                descripNum = "King";
            } else if (number.equals("Q")) {
                descripNum = "Queen";
            } else if (number.equals("J")) {
                descripNum = "Jack";
            } else if (number.equals("A")) {
                descripNum = "Ace";
            }
        } else {
            return "Unknown";
        }
        return descripNum + " of " + descripSuit;
    }
}
