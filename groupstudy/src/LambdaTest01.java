import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;

public class LambdaTest01 {
  public static void main(String[] args) {
    // Runnable
    // - 매개변수와 리턴이 없는 메소드를 가지는 함수형 인터페이스
    // - 동작 메소드는 run()

    // Consumer<T>
    // - 매개변수가 한 개 있고 리턴값이 없는 메소드를 가지는 함수형 인터페이스
    // - 동작 메소드는 accept()

    // Supplier<T>
    // - 매개변수가 없고 리턴값이 있는 메소드를 가지는 함수형 인터페이스
    // - 동작 메소드는 get()

    // Function<T, R>
    // - 일반적인 함수의 형태, 매개변수와 리턴값이 하나씩 존재
    // - 동작 메소드는 apply()

    // Predicate<T>
    // - 매개변수가 한 개 있고 리턴값으로 boolean 타입을 가지는 메소드를 가지는 함수형 인터페이스
    // - 동작 메소드는 test()
    Runnable r = () -> System.out.println("파라미터가 없고 리턴값도 없음");
    Consumer<String> c = str -> System.out.println(str);
    Supplier<String> s = () -> "파라미터가 없고 리턴값이 있음";
    Function<String, String> f = str -> str;
    Predicate<String> p = str -> str.length() == 0;

    System.out.print("Runnable  - run()    : ");
    r.run();

    System.out.print("Consumer  - accept() : ");
    c.accept("파라미터가 있고 리턴값이 없음");

    System.out.print("Supplier  - get()    : ");
    System.out.println(s.get());

    System.out.print("Function  - apply()  : ");
    System.out.println(f.apply("파라미터가 있고 리턴값도 있음"));

    System.out.print("Predicate - test()   : ");
    System.out.println(p.test("문자열 길이가 0인가?"));
  }
}
