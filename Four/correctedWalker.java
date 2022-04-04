import java.util.ArrayList;

public class correctedWalker {
    public int x = 0;
    public int y = 0;
    public int countsteps = 0;
    public void walk() { // accidently put static instead of void
        int singlestep = (int)(Math.random() * 4);
        if (singlestep == 0) {
            x++; // since the method is static, it doesn't recognize my variables
        } else if (singlestep == 1) {
            x--;
        } else if (singlestep == 2) {
            y++;
        } else if (singlestep == 3) {
            y--;
        } countsteps++;
    }
    public int steps() {
        return countsteps;
    }
    public double howFar() {
        return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2)); //fixed power of 2
    } public static void main(String[] args) {
        int steps =  Integer.parseInt(args[0]); // parsed the int
        int numWalkers = Integer.parseInt(args[1]); // parsed int

        ArrayList<Walker> walkers = new ArrayList<Walker>(); // changed arraylist from integer to walker
        for (int j = 0; j < numWalkers; j++) { // added to walkers
            walkers.add(new Walker());
        }
        double average = 0; // never added to count, causing division by zero
        for (int i = 0; i < steps; i++) {
            for (Walker w : walkers) { // never added to walkers
                w.walk(); // doesn't work
            }
        }
        average /= numWalkers;

    }
}