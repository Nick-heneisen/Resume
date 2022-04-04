import java.util.Random; //import random

public class DrunkardsWalk {
    public static void main(String[] args) {
        Random rand = new Random();
        System.out.println("A Drunkard stumbles by ...");
        int x = 0;
        int y = 0;
        for (int i = 0; i < 100; i++) {
            int direction = rand.nextInt(4);
            if (direction == 0) {
                y -= 1;
                System.out.println("South, (" + x + ", " + y + ")");
            } else if (direction == 1) {
                y += 1;
                System.out.println("North, (" + x + ", " + y + ")");
            } else if (direction == 2) {
                x -= 1;
                System.out.println("East, (" + x + ", " + y + ")");
            } else if (direction == 3) {
                x += 1;
                System.out.println("West, (" + x + ", " + y + ")");
            }
        }
    }
}
