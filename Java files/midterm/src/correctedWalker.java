import java.util.ArrayList;

public class correctedWalker {
    public int x = 0;
    public int y = 0;
    public int countsteps = 0;
    public void walk() { // accidently put static instead of void (-0.5 points)
        int singlestep = (int)(Math.random() * 4);
        if (singlestep == 0) {
            x++; // since the method is static, it doesn't recognize my variables (-0.5)
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
        return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2)); //fixed power of 2 (-1)
    } public static void main(String[] args) {
        int steps =  Integer.parseInt(args[0]); // parsed the int
        int numWalkers = Integer.parseInt(args[1]); // parsed int

        ArrayList<correctedWalker> walkers = new ArrayList<correctedWalker>(); // changed arraylist from integer to walker
        for (int j = 0; j < numWalkers; j++) { // added to walkers
            walkers.add(new correctedWalker());
        }
        double average = 0;
        for (int i = 0; i < steps; i++) { // improved system to walk
            for (correctedWalker w : walkers) {
                w.walk();
            }
        }
        average /= numWalkers;
    }
}