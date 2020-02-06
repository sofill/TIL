import java.util.function.Function;

public class LambdaTest04 {
  public static void main(String[] args) {
    // 함수형 인터페이스를 이용한 메소드 참조
    // - 기존에 정의되어 있던 메소드들을 함수형 인터페이스를 통해 참조할 수 있다.
    // - 간단한 예제로 String 데이터를 int 형으로 변환해주는 parseInt() 메소드가 있다.
    // - 이 메소드는 입력으로 String을 필요로 하고 리턴으로 Integer를 사용한다.
    // - 따라서 하나의 입력과 하나의 반환값을 가지므로 Function 인터페이스를 사용할 수 있다.
    // - 단, 기존에 있던 메소드 참조를 진행할 때는 (::)를 사용한다.

    Function<String, Integer> f1 = s -> Integer.parseInt(s);
    Integer res1 = f1.apply("12345");
    System.out.println(res1);

    // 위의 코드는 아래와 같이 간략하게 표현할 수 있다.
    Function<String, Integer> f2 = Integer::parseInt;
    Integer res2 = f2.apply("67890");
    System.out.println(res2);

  }
}
