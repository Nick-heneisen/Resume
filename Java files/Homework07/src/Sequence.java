import java.util.ArrayList;
import java.util.Collections;

public class Sequence {
    private ArrayList<Integer> values;
    public Sequence() {values = new ArrayList<Integer>();}
    public void add(int n) {values.add(n);}
    public String toString() {return values.toString();}
    public Sequence append(Sequence other) {
        Sequence c = new Sequence();
        for (int i : values) {
            c.add(i);
        }
        for (int i : other.values) {
            c.add(i);
        }
        return c;
    }

    public Sequence merge(Sequence other) {
        Sequence c = new Sequence();
        int count = 0;
        for (int i : values) {
            c.add(i);
            if (count < other.values.size()) {
                c.add(other.values.get(count));
            }
            count++;
        }
        return c;
    }

    public Sequence mergeSorted(Sequence other) {
        Sequence c = new Sequence();
        int count = 0;
        int count1 = 1;
        while (count < values.size() && count1 < other.values.size()) {
            if (values.get(count) <= other.values.get(count1))
                c.add(values.get(count++));
            else
                c.add(other.values.get(count1++));
        }
        while (count < values.size())
            c.add(values.get(count++));
        while (count1 < other.values.size())
            c.add(other.values.get(count1++));
        return c;
    }

    public static void main(String[] args) {
        Sequence a = new Sequence();
        Sequence b = new Sequence();

        a.add(1); a.add(3); a.add(5); a.add(7); a.add(9); a.add(11);
        System.out.println(a);
        b.add(2); b.add(4); b.add(6); b.add(8); b.add(10); a.add(12); a.add(13); a.add(13);
        System.out.println(b);

        System.out.println(a.append(b));
        System.out.println(a.merge(b));
        System.out.println(a.mergeSorted(b));

    }
}