import java.util.Scanner;

public class C {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String line = sc.nextLine();
    int tests = Integer.parseInt(line);
    for (int i = 0; i < tests; ++i) {
      System.out.printf("Case #%d: ", i+1);
      solve(sc);
      System.out.println();
    }
  }

  public static void solve(Scanner sc) {
    String[] w = sc.nextLine().split(" ");
    int f = Integer.parseInt(w[0]);
    int d = Integer.parseInt(w[1]);
    int b = Integer.parseInt(w[2]);

    System.out.print(maxF(d, b) + " ");
    System.out.print(minD(f, b) + " ");
    System.out.print(minB(f, d));
  }

  public static long maxF(long D, long B){
    long add = 1;
    long f = 0;
    for (long b = 0; b < Math.min(D, B); ++b) {
      add = add * (D - b) / (b+1);
      f += add;
      if ( f > 4294967295L ) {
        return -1;
      }
    }
    return f;
  }

  public static long minD(long F, long B){
    long d = 1;
    long low = 1;
    long high = F;
    if (B == 1) {
      return F;
    }

    while (high - low > 1) {
      d = (low + high) / 2;
      long f = maxF(d, B);
      if (f < 0 || f >= F){
        high = d;
      }
      else {
        low = d;
      }
    }
    return high;
  }

  public static long minB(long F, long D){
    long b = 1;
    long low = 1;
    long high = D;
    if (D >= F) return 1;

    while ( high - low > 1) {
      b = (low + high) / 2;
      long f = maxF(D, b);
      if ( f < 0 || f >= F) {
        high = b;
      }
      else {
        low = b;
      }
    }

    return high;
  }

}
