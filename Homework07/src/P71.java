import java.util.ArrayList;
import java.util.Random;

public class P71 {
    public static void main(String[] args) {
        Random r = new Random();
        ArrayList<Integer> rolls = new ArrayList<Integer>();
        boolean inRun = false;
        for (int j = 0; j < 21; j++) { rolls.add(r.nextInt(6) + 1); }
        int count = 0;
        int previous = 0;
        for (int i : rolls) {
            if (inRun) {
                if (i != previous) {
                    inRun = false;
                    System.out.print(" ) ");
                }
            }
            if (!inRun) {
                if (count != 20) {
                    if (i == rolls.get(count + 1)) {
                        inRun = true;
                        System.out.print(" ( ");
                    }
                }
            }
            previous = i;
            count++;
            System.out.print(" " + i + " ");
        }
        if (inRun) { System.out.print(" ) ");}
    }
}
