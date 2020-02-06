# Networking 개론



LessonManagementSystem (이하 LMS)가 있다. 해당 시스템은 데이터를 파일로 다루며, 여러명의 사용자가 이를 사용한다. 만약 네트워킹 기술이 없다면 각각의 로컬 컴퓨터에 LMS 어플리케이션이 따로 존재하며, 각 로컬에 데이터 파일이 따로 존재하게 된다.  즉, 한 사용자가 다룬 데이터를 다른 사용자가 공유할 수 없다.

- 수업 관리 시스템 존재 이유 자체가 사라진다.



#### 해결책 1 )

- 네트워크 드라이브를 통해 여러 명의 사용자가 파일을 공유하는 형태를 사용한다.
- 단, 사용자는 동일한 네트워크 드라이브에 접근할 수 있어야한다.
- 이 방법의 문제점은 한 명의 사용자가 파일을 수정할 때, 다른 사용자가 해당 파일을 수정하려는 경우, 즉 동시에 파일에 접근하여 특정 작업을 수행하는 경우 문제가 발생한다.



#### 해결책 2 )

- FILE I/O 프로그램을 하나 만들고 이 프로그램이 파일에 대한 모든 기능을 다룬다.
- 사용자는 LMS를 통해 해당 FILE I/O 프로그램에 데이터에 대한 요청을 하고 프로그램은 적절한 응답을 반환한다.
- 즉 이 프로그램은 파일관리, 요청처리 등의 기능(CRUD)을 가진다.



어플리케이션간 communication에서 한 어플리케이션이 다른 어플리케이션에게 요청을 보내고 요청을 받은 어플리케이션이 적절한 응답을 주는 형태를 서버-클라이언트 형태라 칭하며 서버와 클라이언트간 적절한 통신 방법이 존재해야 한다. 이를 전체적으로 네트워크 프로그래밍이라 한다. 

추가)

- 서버 프로그램이 존재하는 영역의 메모리에 클라이언트는 직접 접근할 수 없다. 
- 따라서 request - response 형태로 데이터가 전달되는데, 이를 네트워킹이라 한다.
- 즉, 프로그램 사이에 데이터를 주고받는 기술이, 좀 더 풀어서 서버와 클라이언트 프로그램에서 데이터가 전달되는 기술을 네트워킹이라 한다.



클라이언트는 요청을 보내는 프로그램이며 서버는 요청을 받아 적절한 응답을 반환하는 프로그램이다. 이 둘은 상대적인 개념이며 아래와 같이 적절한 예시를 들 수 있다.

- 각 사용자의 스마트폰 단말기에 설치된 카카오톡 프로그램은 클라이언트이다.
- 다음카카오 회사에는 서버가 존재한다.
- 한 사람이 어플리케이션(클라이언트)를 통해 다른사람에게 메시지를 보내면 해당 메시지는 카카오 서버에 전송된다.
- 카카오 서버에서는 해당 요청이 어느 사용자에게 전달되어야 되는지 판단하여 다시 목적 클라이언트에게 메시지를 전송한다.

---

---

#### 프로젝트에서의 흐름도

App을 분리하여 서버, 클라이언트 역할을 수행하는 ServerApp과 ClientApp을 만든다. 클라이언트는 서버에게 요청을 하고 서버는 클라이언트의 요청을 받아 적절한 응답을 반환한다. 우리의 클라이언트가 보내는 요청을 보통 CRUD이며 서버는 해당 요청을 받아 파일로부터 데이터를 적절히 연산하여 응답을 반환한다. 클라이언트와 서버의 일을 정리하면 아래와 같다.

클라이언트 )

- 사용자 UI 처리

서버 )

- Data 처리



아래와 같이 실습을 진행한다. 

1. 프로젝트 생성
   - guide-project-server
   - guide-project-client
2. 

---

---

1. 프로젝트 생성

```bash
# 터미널상에서
mkdir guide-project-client
mkdir guide-project-server

cd guide-project-client/
gradle init # gradle 프로젝트 초기화
# 2, 3, 1, 1, default(enter), com.eomcs.lms 순서로 입력
```



build.grade 수정

```groovy
plugins {
    id 'java'
    id 'eclipse'
}
tasks.withType(JavaCompile) {
    options.encoding = 'UTF-8'
    sourceCompatibility = '1.8'
    targetCompatibility = '1.8'
}
repositories {
    jcenter()
}
dependencies {
    implementation 'com.google.guava:guava:28.0-jre'
    testImplementation 'junit:junit:4.12'
}
```



```bash
# 터미널상에서
gradle eclipse # 이클립스 프로젝트 초기화
```



```bash
# 이클립스에서
file - import - existing - guide-project-client 추가
App.java >> ClientApp.java 변경
src/main/resources/README.md 추가
README.md 내용 추가(자바 어플리케이션이 사용할 기타 자원을 두는 폴더)
README.md 복사해서 src/test/resources에 복사 및 내용 수정 (자바 단위테스트에서 사용할 기타 자원을 두는 폴더)
#README.md 수정시에는 markdown source 탭에서 해야함

AppTest.java >> ClientAppTest.java 변경
소스 내용은 주석처리
```



```java
// ClientApp.java
package com.eomcs.lms;

public class ClientApp {
    public static void main(String[] args) {
      System.out.println("클라이언트 수업 관리 시스템입니다.");
    }
}
```