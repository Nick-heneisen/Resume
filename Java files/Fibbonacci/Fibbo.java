
public class Fibbo {
    public static void main(String[] args) {
        for (int i = 2; i < 20; i++) {
        System.out.println(i + ": " + Fibbo.nick(7, 1, 1));
        }
    }

    public static int nick(int index, int previous, int answer) {
        if (index == 0) return answer;
        return nick(index - 1, answer, answer + previous);
    }
}