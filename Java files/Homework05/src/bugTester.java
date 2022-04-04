public class bugTester {
    public static void main(String[] args) {
        Bug buggy = new Bug(0);

        System.out.println("Buggy starts at " + buggy.getPosition() + ".");
        buggy.move();
        buggy.move();
        buggy.move();
        System.out.println("Buggy moves 3 steps to the right. He is now at " + buggy.getPosition() + ".");
        buggy.turn();
        buggy.move();
        System.out.println("Buggy turns around and takes 1 step left. He is now at " + buggy.getPosition() + ".");
        System.out.println("Buggy dies from a russian invasion to Ukraine. Poor buggy!");
    }
}
