import java.util.ArrayList;

public class Walker {
    public int x = 0;
    public int y = 0;
    public int countsteps = 0;
    public static walk(int steps) { // accidently put static instead of void (-0.5)
        for (int i = 0; i < steps; i++) {
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
    }
    public int steps() {
        return countsteps;
    }
    public double howFar() {
        return Math.sqrt(Math.pwr2(x) + Math.pwr2(y)); //didn't correctly take the power of 2 (-1)
    } public static void main(String[] args) {
        Walker a = new Walker();
        int steps = args[0]; // didn't convert args to an int (-1)
        int numWalkers = args[1]; // didn't convert args to an int (-1)
        ArrayList<int> walkers = new ArrayList<int>(); // put int instead of integer (-0.5)
        double average = 0; double sum = 0; int count = 0; // since walkers is empty, count is never added to (-1)
        for (int i : walkers) { // never added to walkers (-3)
            sum += i.howFar; count++; // doesn't work (-3)
        }
        average = sum/count;
        a.walk(countsteps); // doesn't work (-2)
    }
}
