# 32_07 - Data 처리 코드를 별도의 클래스로 정의하여 객체화 시키기
(서버꺼)

## 학습목표

- DAO (Data Access Object) 의 역할과 이점을 이해한다.
- 데이터 처리 코드를 DAO로 분리할 수 있다. 

### DAO

- 데이터 처리 역할을 수행하는 객체이다.
- 데이터 처리 방식을 캡슐화하여(= 추상화하여 = 클래스로 정의하여) 객체의 사용을 일관성 있게 만든다. 
	- 즉 데이터 처리 방식(배열이냐, 스택이냐, 큐냐, 맵이냐 등)을 클래스로 포장(캡슐화)하면
	  데이터 처리 방식에 상관없이 메서드 사용을 통일할 수 있다.  


## 실습 소스 및 결과

- src/main/java/com/eomcs/lms/dao 패키지 생성
- src/main/java/com/eomcs/lms/dao/BoardObjectFileDao.java 추가
- src/main/java/com/eomcs/lms/dao/LessonObjectFileDao.java 추가
- src/main/java/com/eomcs/lms/dao/MemberObjectFileDao.java 추가
- src/main/java/com/eomcs/lms/ServerApp.java 변경


## 실습  

### 훈련 1: 게시물 데이터를 처리할 DAO 클래스를 정의하라.

- com.eomcs.dao 패키지를 생성한다. 
- com.eomcs.lms.BoardObjectFileDao 클래스를 정의한다.  

### 훈련 2: BoardFileDao 객체를 적용하라.  

- com.eomcs.lms.DataLoaderLisetener 를 변경한다.
	- 게시물 데이터를 로딩하고 저장하는 기존 코드를 제거한다.
	- 대신에 BoardFileDao 객체를 생성한다.
- com.eomcs.lms.App 을 변경한다. 
	- Map 에서 BoardFileDao 를 꺼내 관련 커맨드 객체에 주입한다.
- BoardXxxServlet 을 변경한다.
	- 생성자에서 List 객체를 받는 대신에 BoardFileDao 객체를 받는다.
	- 데이터를 저장하고, 조회하고, 변경하고, 삭제할 때 BoardFileDao 객체를 통해 처리한다. 
	
	