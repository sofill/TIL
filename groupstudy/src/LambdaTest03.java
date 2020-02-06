import java.util.function.BinaryOperator;
import java.util.function.UnaryOperator;

public class LambdaTest03 {
  public static void main(String[] args) {
    // UnaryOperator<T>
    // - Function의 자손
    // - 차이점은 매개변수와 리턴의 타입이 같다.

    // BinaryOperator<T>
    // - BiFunction의 자손
    // - 차이점은 매개변수와 리턴의 타입이 같다.
    UnaryOperator<Integer> uo = i -> i * i;
    BinaryOperator<Integer> bo = (i, j) -> (int) Math.pow(i, j);

    System.out.print("UnaryOperator  - apply()  : ");
    System.out.println(uo.apply(3));

    System.out.print("BinaryOperator - apply()  : ");
    System.out.println(bo.apply(2, 3));
  }
}
