# spring _ 김영한 _ 스프링입문 _ 1강

### 프로젝트 생성하기

- spring boot 기본 생성도구를 이용 => https://start.spring.io/

  <img src = "./spring _ 김영한 _ 스프링입문 _ 1강.assets/spring _ 김영한 _ 스프링입문 _ 1강.png "/>

### maven vs gradle

- build 및 라이브러리를 관리하는 툴

- 예전에 legacy 프로젝트들은 maven, 요즘 프로젝트들은 gradle들을 사용하는 추세 

  

### language

- java

  

### Spring boot

- snapshot, m1 등은 정식 릴리즈 된 버전이 아님.
- 정식버전 중 가장 버전을 채택하면 될듯



### Project Metadata

- Group : 기업주소, 없다면 아무거나
- Artifact : 어떠한 결과물을 표시, 프로젝트 명이라 생각하면 됌.



### Dependencies

- 어떤 라이브러리를 쓸지 먼저 설정해줄 수 있음.
- spring web : 스프링을 이용한 웹프로젝트 생성
- thymeleaf : template 엔진, 템플릿을 구성함, 회사마다 다름



모든 게 완료되었다면, generate로 생성 후 원하는 위치에 압축을 해제하자

------



### open spring

- intellij `open or import`를 이용하여 열자 (open as project)
- 첫 로딩 시 굉장히 많은 프로그램을 자동으로 다운함. (인터넷 연결 필수)



### folder tree 

<img src = "./spring _ 김영한 _ 스프링입문 _ 1강.assets/spring _ 김영한 _ 스프링입문 _ 1강_1.png"/>

- graddle : graddle 관련 폴더
- src/main/java : 실제  package와 source 파일들이 존재
- src/main/resources : 실제  xml, properties, html등 java가 아닌 모든 파일들
- src/test : test와 관련된 코드들 << 요즘 개발 환경에서는 중요
- build.gradle 
  - version과 라이브러리 관리, 요즘은 spring boot과 만들어줌
  - dependencies : 설치한 라이브러리들
  - repositories : maveCentral() 에서 위 dependencies를 다운받으라 지정( 다른 곳도 가능)
- gradlew : build 관련



### 실행

- main 함수를 run (초록 화살표 누르면 된다.)
- 하얀창에 글씨 써지면 제대로 성공한 것



cf). graddle을 이용한 실행 대신 intellij로 바로 실행하기

- ctrl +alt +s 로 설정 창 들어가기
- gradle 검색
- 중앙에  `build and run using`, `run tests using`을 intelllij idea로 바꿔주기 

<img src="./spring _ 김영한 _ 스프링입문 _ 1강.assets/spring _ 김영한 _ 스프링입문 _ 1강2.png"/>



### 추가정보

- annotation : 주석이라는 사전적 의미로 영향을 주지 않으나 의미를 나태내 줌.



### 참고문서

- 인프런, 스프링 입문 - 코드로 배우는 스프링 부트, 웹 MVC, DB 접근 기술, 김영한 강사님