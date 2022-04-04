public class R530 {
    public static void main(String[] args) {
        System.out.println(a());
        System.out.println(b());
        System.out.println(c());
        System.out.println(d());
        System.out.println(e());
        System.out.println(f());
    }
    public static boolean a() {
        boolean b = false;
        int x = 0;
        return b && x == 0; // b is false, x is 0 (true), true and false is false
    }
    public static boolean b() {
        boolean b = false;
        int x = 0;
        return b || x == 0; // false or true is true
    }
    public static boolean c() {
        boolean b = false;
        int x = 0;
        return !b && x == 0; // not false is true, true and true is true
    }
    public static boolean d() {
        boolean b = false;
        int x = 0;
        return !b || x == 0; // not false is true, true or true is true
    }
    public static boolean e() {
        boolean b = false;
        int x = 0;
        return b && x != 0; // false and false is false
    }
    public static boolean f() {
        boolean b = false;
        int x = 0;
        return b || x != 0; // false or false is false
    }
    public static boolean g() {
        boolean b = false;
        int x = 0;
        return !b && x != 0; // true and false is false
    }
    public static boolean h() {
        boolean b = false;
        int x = 0;
        return !b || x != 0; // true or false is true
    }

}
