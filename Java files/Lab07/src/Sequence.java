public class Sequence
{
    private int[] values;
    public Sequence(int size) { values = new int[size]; }
    public void set(int i, int n) { values[i] = n; }
    public int get(int i) { return values[i]; }
    public int size() { return values.length; }

    //e7.11
    public static void main(String[] args) {
        Sequence one = new Sequence(10);
        one.set(0, 84);
        one.set(1, 10);
        one.set(2, 69);
        one.set(3, 12);
        one.set(4, 22);
        one.set(5, 10);
        one.set(6, 4000000);
        one.set(7, 12);
        one.set(8, 22);
        one.set(9, 88);

        Sequence two = new Sequence(10);
        two.set(0, 84);
        two.set(1, 10);
        two.set(2, 69);
        two.set(3, 12);
        two.set(4, 22);
        two.set(5, 10);
        two.set(6, 4000000);
        two.set(7, 12);
        two.set(8, 22);
        two.set(9, 88);

        System.out.println("One is equal to two: " + one.equals(two));
        System.out.println("One has the same values as two: " + one.sameValues(two));
        System.out.println("One plus two is: ");
        for (int i = 0; i < 10; i++) {
            System.out.println(one.sum(two).get(i) + " ");
        }
    }

    public boolean equals(Sequence other) {
        boolean result = true;
        for (int i = 0; i < other.size(); i++) {
            if (other.get(i) != this.get(i)) {
                result = false;
            }
        }
        return result;
    }

    //e7.12
    public boolean sameValues(Sequence other) {
        boolean result = true;
        int compare;
        for (int i = 0; i < other.size(); i++) {
            compare = this.get(i);
            for (int j = 0; j < other.size(); j++) {
                if (other.get(j) == compare) {
                    result = true;
                    break;
                } else {
                    result = false;
                }
            }
            if (result == false) {
                return result;
            }
        }
        return result;
    }

    //e7.14
    public Sequence sum(Sequence other) {
        boolean larger = true;
        Sequence add = new Sequence(0);
        if (this.size() >= other.size()) {
            add = new Sequence(this.size());
        } else {
            add = new Sequence(other.size());
        }
        int sum = 0;
        for (int i = 0; i < add.size(); i++) {
            if (this.size() > other.size()) {

            }
            sum = this.get(i) + other.get(i);
            add.set(i, sum);
            sum = 0;
        }
        return add;
    }
}
