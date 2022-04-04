public class LispTest {
    public static void main(String[] args) {
        LispList testList = LispList.NIL.cons("A").cons("B").cons("C");
        System.out.println("Expected result is A B C");
        System.out.println(testList);
        System.out.println("Length test exected 3");
        System.out.println(testList.length());

    }
}
