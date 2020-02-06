import java.util.function.BiConsumer;
import java.util.function.BiFunction;
import java.util.function.BiPredicate;

public class LambdaTest02 {
  public static void main(String[] args) {
    // BiConsumer<T, U>
    // - 두 개의 매개변수가 있고 반환값은 없음
    // - 동작 메소드는 accept()

    // BiFunction<T, U, R>
    // - 두 개의 매개변수와 하나의 반환값을 가짐
    // - 동작 메소드는 apply()

    // BiPredicate<T, U>
    // - 두 개의 매개변수와 하나의 boolean 타입 반환값을 가짐
    // - 동작 메소드는 test()
    BiConsumer<String, String> bc = (s1, s2) -> System.out.printf("%s : %s\n", s1, s2);
    BiFunction<String, String, Boolean> bf = (s1, s2) -> s1.equals(s2);
    BiPredicate<String, Integer> bp = (s, i) -> s.length() == i;

    System.out.print("BiConsumer  - accept() : ");
    bc.accept("이름", "김용휘");

    System.out.print("BiFunction  - apply()  : ");
    System.out.println(bf.apply("문자열 같음 판단", "문자열 같음 판단"));

    System.out.print("BiPredicate - test()   : ");
    System.out.println(bp.test("문자열길이", 5));
  }
}
