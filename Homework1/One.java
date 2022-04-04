import java.math.BigInteger; 

public class One {
  public static void main(String[] args) {
    int n = Integer.parseInt(args[0]); 
    System.out.println(fun(BigInteger.valueOf(n)));  // 1 1 2 3 5 8 13 21 34 55 89 
                                                     // 0 1 2 3 4 5  6  7  8  9 10 
  }
  public static BigInteger fun(BigInteger index) {
    if (index == new BigInteger("0")) return new BigInteger("1"); 
    else if (index == new BigInteger("1")) return new BigInteger("1"); 
    return funHelper(new BigInteger("1"), index, new BigInteger("1"), new BigInteger("1")); 
  }
  public static BigInteger funHelper(BigInteger location, 
                                   BigInteger target, 
                                   BigInteger a, 
                                   BigInteger b) {
    if (location.equals(target)) return b; 
    else System.out.println(b);
      return funHelper(location.add(new BigInteger("1")), target, b, a.add(b));   
    }
}