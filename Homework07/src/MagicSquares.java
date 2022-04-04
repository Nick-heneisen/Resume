import java.util.ArrayList;

public class MagicSquares {
    //initialises stuff
    public static void main(String[] args) {
        MagicSquares a = new MagicSquares();
        boolean magic = false;
        ArrayList<Integer> first = new ArrayList<Integer>();
        ArrayList<Integer> second = new ArrayList<Integer>();
        ArrayList<Integer> third = new ArrayList<Integer>();
        ArrayList<Integer> fourth = new ArrayList<Integer>();
        ArrayList<Integer> full = new ArrayList<Integer>();

        //puts in 4 lists for each row, and 1 for the full list
        for (int i = 0; i < 4; i++) {
            first.add(Integer.parseInt(args[i]));
        }
        for (int i = 4; i < 8; i++) {
            second.add(Integer.parseInt(args[i]));
        }
        for (int i = 8; i < 12; i++) {
            third.add(Integer.parseInt(args[i]));
        }
        for (int i = 12; i < 16; i++) {
            fourth.add(Integer.parseInt(args[i]));
        }
        for (int i = 0; i < 16; i++) {
            full.add(Integer.parseInt(args[i]));
        }

        //checks if it has 1 - 16
        for (int i = 1; i < 17; i++) {
            if (full.contains(i)); { full.remove(Integer.valueOf(i)); }
        }
        //checks if the sums are equal
        if (full.isEmpty()) {
            int magicValue = first.get(0) + second.get(0) + third.get(0) + fourth.get(0);
            for (int i = 0; i < 4; i++) {
                if (first.get(i) + second.get(i) + third.get(i) + fourth.get(i) == magicValue) {
                    if (a.sum(first) + a.sum(second) + a.sum(third) + a.sum(fourth) == magicValue * 4) {
                        if (first.get(0) + second.get(1) + third.get(2) + fourth.get(3) == magicValue) {
                            if (first.get(3) + second.get(2) + third.get(1) + fourth.get(0) == magicValue) {
                                magic = true;
                            }
                        }
                    }
                }
            }
        }

        // prints if it is or not
        if (magic) {
            System.out.println("This is a magic square. :)");
        } else {
            System.out.println("This is not a magic square. :(");
        }
    }

    //sums an arraylist
    public int sum(ArrayList<Integer> list) {
        int sum = 0;
        for (Integer integer : list) { sum += integer; }
        return sum;
    }
}
