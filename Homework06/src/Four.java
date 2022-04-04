public class Four {
    public static void main(String[] args) {
        int size = Integer.parseInt(args[0]);
        for (int line = 0; line < size; line++) {
            for (int column = 0; column < size; column++) {
                if (line + column == size / 2 || line == size / 2 || column == size / 2)
                    System.out.print("* ");
                else System.out.print("  ");
            }
            System.out.println();
        }
    }
}
