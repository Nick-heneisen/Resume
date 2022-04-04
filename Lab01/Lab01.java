import java.math.*;

public class Lab01 {
  public static void main(String[] args) {
    BigDecimal a = new BigDecimal("1");
    BigDecimal b = new BigDecimal("2");
    BigDecimal c = new BigDecimal("3");

    System.out.println(a.add(b)); // 1 + 2
    System.out.println(b.multiply(c)); // 2 * 3
    System.out.println(a.add(b.add(c.add(new BigDecimal("4"))))); // (1 + (2 + (3 + 4)))
    System.out.println(a.add(b.add(c.add(new BigDecimal("4"))))); // 1 + 2 + 3 + 4
    System.out.println((b.multiply(c)).add((new BigDecimal("4")).multiply(new BigDecimal("5")))); // 2 * 3 + 4 * 5
  }
}