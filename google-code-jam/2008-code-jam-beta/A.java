import java.util.Scanner;

public class A {

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
    double x1 = Double.parseDouble(w[0]);
    double y1 = Double.parseDouble(w[1]);
    double x2 = Double.parseDouble(w[2]);
    double y2 = Double.parseDouble(w[3]);
    double x3 = Double.parseDouble(w[4]);
    double y3 = Double.parseDouble(w[5]);

    // System.out.println(x1+" "+ y1+" "+ x2+" "+ y2+" "+ x3+" "+ y3);

    double[] s = sides(x1, y1, x2, y2, x3, y3);
    if (isTriangle(x1, y1, x2, y2, x3, y3)) {
      System.out.print(isIso(s) ? "isosceles " : "scalene ");
      System.out.print(angle(s) + " ");
      System.out.print("triangle");
    }
    else {
      System.out.print("not a triangle");
    }

  }

  public static boolean isTriangle(double x1, double y1, double x2, double y2, double x3, double y3) {
     if ( (x3-x1)*(y2-y1) - (x2-x1)*(y3-y1) == 0 )
       return false;
     return true;
  }

  public static boolean isIso(double[] s) {
    if (Math.abs(s[0] - s[1]) < 1e-12 || 
        Math.abs(s[1] - s[2]) < 1e-12 || 
        Math.abs(s[0] - s[2]) < 1e-12    )
      return true;
    return false;
  }

  public static String angle(double[] s) {
    double maxS = 0;
    int idx = -1;
    for (int i = 0; i < 3; ++i) {
      if (s[i] > maxS) {
        maxS = s[i];
        idx = i;
      }
    }
    double sumMinS = 0;
    for (int i = 0; i < 3; ++i) {
      if (i != idx) {
        sumMinS = sumMinS + (s[i] * s[i]);
      }
    }
    double right = Math.sqrt(sumMinS);
    if (Math.abs(maxS - right) < 1e-12 ) {
      return "right";
    }
    else if (maxS > right) {
      return "obtuse";
    }
    return "acute";
  }

  public static double[] sides(double x1, double y1, double x2, double y2, double x3, double y3) {
    double[] s = new double[3];

    s[0] = Math.sqrt( Math.abs(x1-x2) * Math.abs(x1-x2) + Math.abs(y1-y2)*Math.abs(y1-y2) );
    s[1] = Math.sqrt( Math.abs(x1-x3) * Math.abs(x1-x3) + Math.abs(y1-y3)*Math.abs(y1-y3) );
    s[2] = Math.sqrt( Math.abs(x3-x2) * Math.abs(x3-x2) + Math.abs(y3-y2)*Math.abs(y3-y2) );
    
    return s;
  }

}
