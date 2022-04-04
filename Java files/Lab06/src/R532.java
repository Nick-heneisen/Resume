public class R532 {
    public static void main(String[] args) {
        //part a
        //n is 0, then n == 0 is true, which is what b should be
        //n is 5, then n == 0 is true, which is what b should be
        boolean b;
        int n = 0;
        b = (n == 0);
        System.out.println(b);
        if (n == 0) {
            b = true;
        } else {
            b = false;
        }
        System.out.println(b);

        //part b
        n = 0;
        b = (n != 0);
        if (n == 0) {
            b = false;
        } else {
            b = true;
        }
        System.out.println(b);

        n = 16;
        b = (n != 0);
        if (n == 0) {
            b = false;
        } else {
            b = true;
        }
        System.out.println(b);

        // part c
        b = false;
        if (n > 1) {
            if (n < 2) {
                b = true;
            }
        }
        n = 1;
        System.out.println(b);

        //b = false;

        //part d
        if (n < 1) {
            b = true;
        } else {
            b = (n > 2);
        }
        b = (n != 2) && (n != 1);
        n = 1;
        System.out.println(b);
    }
}
