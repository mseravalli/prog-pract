import java.util.*;

public class B {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String line = sc.nextLine();
    int tests = Integer.parseInt(line);
    for (int i = 0; i < tests; ++i) {
      System.out.printf("Case #%d:", i+1);
      solve(sc);
      System.out.println();
    }
  }

  public static void solve(Scanner sc) {
    String[] name = sc.nextLine().split(" ");
    String[] priceStr = sc.nextLine().split(" ");
    Integer[] price = new Integer[priceStr.length];
    boolean[] used = new boolean[priceStr.length];
    for (int i = 0; i < priceStr.length; ++i) {
      price[i] = Integer.parseInt(priceStr[i]);
      used[i] = true;
    } 
    TreeMap<String, Integer> m = new TreeMap<String, Integer>();
    for (int i = 0; i < priceStr.length; ++i) {
      m.put(name[i], i);
    }
    
    long k= maxSubseq(used, price);

    for(Map.Entry<String, Integer> e : m.entrySet()) {
      used[e.getValue()] = false;
      if (maxSubseq(used, price) == k) {
        System.out.printf(" %s", e.getKey());
      }
      else {
        used[e.getValue()] = true;
      }
    }   
  }

  public static long maxSubseq(boolean[] used, Integer[] price){
    long res = 0;
    int n = used.length;
    long[] seq = new long[n];
    for (int i = 0; i < n; ++i) {
      seq[i] = 1;
      if (used[i]) {
        for (int j = 0; j < i; ++j) {
          if (used[j] && price[j] < price[i]){
            seq[i] = Math.max(seq[i], seq[j] + 1);
          }
        } 
      }
      res = Math.max(res, seq[i]);
    }
    return res;
  }


}
