# Java Exception Handling

---

#### Error

에러란, 컴퓨터 하드웨어의 오동작 또는 고장으로 인해 응용프로그램에 이상이 생겼거나 JVM 실행에 문제가 생겼을 경우를 말한다.

- 대처할 방법이 제한적이다.



#### Exception

예외란, 사용자의 잘못된 조작 또는 개발자의 잘못된 프로그램 구현으로 인해 발생하는 프로그램 오류를 말한다. 예외가 발생하면 프로그램이 종료된다는 것은 error와 동일하지만 예외는 예외처리를 통해 프로그램을 종료시키지 않고 정상적으로 동작하게 만들 수 있다.

- try ~ catch ~ [finally] 문법을 사용한다.

---

#### 자주 발생하는 예외

| 예외                           | 원인                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| ArithmeticException            | 정수를 0으로 나누는 경우 발생                                |
| ArrayIndexOutOfBoundsException | 배열의 범위를 벗어난 index를 접근할 시 발생                  |
| ClassCastException             | 변환할 수 없는 타입으로 객체를 변환 시 발생                  |
| NullPointException             | 존재하지 않는 레퍼런스를 참조할 때 발생                      |
| IllegalArgumentException       | 잘못된 인자를 전달할 때 발생                                 |
| IOException                    | 입출력 동작 실패 또는 인터럽트 시 발생                       |
| OutOfMemoryException           | 메모리가 부족한 경우 발생                                    |
| NumberFormatException          | 문자열이 나타내는 숫자와 일치하지 않는 타입의 숫자로 변환시 발생 |

---

```java
// 예외처리 문법
try {
    // 에러가 발생할 수 있는 코드를 위치시킨다.
    // try 블럭은 최소한 하나의 catch 블럭을 가져야한다.
    // throw new Exception(); // 강제로 테스트 에러를 발생시킴
} catch (Exception e) {
    // 에러가 발생하면 수행되는 블럭
    // e.printStackTrace();
    // System.out.println(e.getMessage()); 
    // 위와 같은 방법으로 오류 내용을 출력할 수 있음
    // 오류를 출력하는 방법은 여러가지이다.
} catch (ExceptionType ParameterName) {
    // catch 블럭은 여러 개 존재할 수 있으며, 
    // 반드시 java.lang.Throwable의 하위 타입으로 선언되어야 한다.
} finally {
    // 무조건 수행하는 블럭(필수는 아니다.)
    // 보통 finally 블럭에는 사용중인 리소스를 해제하는 작업을 진행한다.
    // ex) 스트림을 close() 하거나 데이터베이스 연결을 끊는다.
}
```

---

#### 예외가 발생한 메소드에서 예외 객체를 호출한 위치로 넘기는 방법(throws)



###### 자바의 예외처리 방법

- 예외가 발생한 지점에서 try ~ catch ~ finally 블럭을 이용하여 직접 처리
- 예외를 호출한 지점으로 전달하여 처리(키워드 throws 사용)



```java
public class ExceptionTest {
    static void callDriver() throws ClassNotFoundException{
        Class.forName("oracle.jdbc.driver.OracleDriver");
        System.out.println("완료");
    }   
    public static void main(String args[]){       
        try{           
            callDriver();       
        }catch(ClassNotFoundException e){
            System.out.println("클래스를 찾을 수 없습니다.");
        }catch(Exception e){
            System.out.println(e.getMessage());
        }finally{
            System.out.println("시스템 종료.");
        }      
    }
}
```

- 클래스를 찾지 못하면 ClassNotFoundException 예외가 발생한다.
- 예외는 callDriver() 메소드에서 발생하지만, ClassNotFoundException 예외가 발생하면 호출한 지점인 main() 메소드로 예외 객체를 전달한다. 
- main() 메소드에서는 예외 객체를 받아 직접 처리하는 것을 볼 수 있다.

---

#### 사용자 정의 예외 만들기(throw)

기존의 예외 처리를 위한 클래스로 예외를 처리할 수 없다면, 사용자가 예외 클래스를 작성할 수 있다.
사용자가 예외 클래스를 직접 정의하려면 최상위 클래스인 java.lang.Exception 클래스를 상속받아 클래스를 구현한다.

`class ClassName extends Exception { ... }`

예외는 사용자가 강제적으로 발생시킬 수 있다. 자바는 예외를 발생시키기 위해 throw 예약어를 사용한다.

`throw new ExceptionClassName(parameter);`

사용자가 강제적으로 예외를 발생시켜도, try ~ catch ~ finally 구문을 이용해 예외 처리를 하거나 throws를 이용하여 예외 객체를 호출 지점으로 전달해야 한다.

```java
public class MyException extends Exception {   
    public MyException() {
        super("내가 만든 예외");
    }
}
public class ExceptionTest {
    static void callException() throws MyException {       
        throw new MyException();
    }   
    public static void main(String args[]){       
        try{
            callException();             
        } catch(MyException e) {
            System.out.println(e.getMessage());
        } catch(Exception e) {
            System.out.println(e.getMessage());
        } finally {
            System.out.println("시스템 종료.");
        }    
    }
}
```



---

#### try ~ with ~ resource

JDK 1.7부터 추가된 문법으로, 주로 입출력(I/O)과 관련된 클래스를 사용할 때 유용하다. 
입출력에 사용되는 클래스 중에서는 사용한 후에 꼭 자원을 해제해야하는 것들이 있다. 
해당 문법은 입출력 처리시 예외가 발생하는 경우 JVM이 자동으로 자원을 해제해준다.

- try() 안의 입출력 스트림을 생성하는 로직을 작성하는데, 이 때 해당 객체는 반드시 AutoCloseable 인터페이스를 구현한 객체여야 한다.

```java
try(FileOutputStream out = new FileOutputStream("exFile.txt")) { 
    // 입출력 로직 처리
} catch(IOException e) { 
    e.printStackTrace();
}
```

---

[예외처리 참고 링크 - 자세히 설명되어 있음](https://pridiot.tistory.com/54)