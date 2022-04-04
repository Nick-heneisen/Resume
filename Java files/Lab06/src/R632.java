public class R632 {
    public static void main(String[] args) {
        int travelNum = (int) (1 + Math.random() * 15);
        if (travelNum >= 1 && travelNum <= 10) {
            System.out.println("California");
        }
        if (travelNum > 10 && travelNum <= 13) {
            System.out.println("Nevada");
        }
        if (travelNum > 13 && travelNum <= 15) {
            System.out.println("Utah");
        }
    }
}
