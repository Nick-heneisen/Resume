import java.util.Random;

public class DiceGame {
    public static void main(String[] args) {
        Random rand = new Random();
        int numof66 = 0; //number of times a double six is rolled
        int finalcount = 0;
        int finalcount2 = 0;
        int numof6 = 0;
        for (int i = 0; i <1000000; i++) {
            for (int j = 0; j < 24; j++) {
                int jimmydice = rand.nextInt(1, 7) + 1;
                int happydice = rand.nextInt(1, 7) + 1;
                if (jimmydice == 6 && happydice == 6) {
                    numof66++;
                }
            }
            if (numof66 >= 1) {
                finalcount++;
            }
            numof66 = 0;
            for (int k = 0; k < 4; k++) {
                int onedice = rand.nextInt(1, 7);
                if (onedice == 6) {
                    numof6++;
                }
            }
            if (numof6 >= 1) {
                finalcount2++;
            }
        }
        System.out.println("I won $" + finalcount + ", but my real total is $" + (finalcount - (1000000 - finalcount)));
        System.out.println("I won " + finalcount + " and lost " + (1000000 - finalcount));
        System.out.println(" ");
        System.out.println("After rolling 1 die 4 times a million times 6 appeared " + finalcount2 + " times.");
    }
}
