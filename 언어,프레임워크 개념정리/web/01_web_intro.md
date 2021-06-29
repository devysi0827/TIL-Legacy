# TIL 0201

## HTML

1. HTML(Hyper Text Markup Language)
   - 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근 할 수 잇는 텍스트
   - 텍스트를 구조화하여 구분하고, 태그 등을 통하여 의미를 부여한다.(Markup)
   - 절대 오류가 발생하지 않고 발생한다면, 레이아웃이 깨진다.



2. DOM(Document Object Model)

   - 웹페이지를 객체 지향적 표현, 문서의 구조적 표현과  그의 접근 가능한 방법을 제공한다.



3. 요소(Element)

   - HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성

   - 각 태그를 중첩하여 사용한다.

   - 내용이 없는 태그들

     - br : 줄바꿈을 위해 사용한다.

     

     - hr: 수평선을 그어준다

       ​	width : 수평선의 길이(px이나 %)을 정한다.

       ​	align : 정렬방식(left, right, center)를 정한다.

       ​	color : 수평선의 색상값을 정한다.

       ​	size : 수평선의 굵기(px)를 정한다.

     

     - img : 이미지를 삽입한다.

       ​	src : 이미지의 경로

       ​	alt : 이미지를 표시할 수 없을 때 출력할 내용

       ​	width : 이미지의 가로 크기

       ​	height : 이미지의 세로 크기

       ​	loading : 이미지 로딩 방식

       

     - link

       ​	href : 링크 주소

       ​	rel : 스타일 시트 관계 표시(더 조사가 필요함)

       ​	target="_blank" : 새 페이지로 링크를 불러옴

     ```html
     link href="style.css" rel="stylesheet" target="_blank">
     ```

     

     - meta

       ​	name: meta 요소의 정보, 제목같은 형태

       ​    content : name의 상세 정보

       ​	

     - input

       [[Html\] input type 종류 & 예제 총정리 (tistory.com)](https://coding-factory.tistory.com/24)

       



4. 속성(Attribute)

   - 태그의 부가적 정보

   - 시작 태그에 위치하며 이름과 값이 쌍을 이룬다

     - ```html
       <p align="center">
       ```

   - 태그와 상관없이 사용 가능한 속성들(html global attribute)도 있다.



5. 시멘틱 태그
   - 가독성이 높아지고 유지보수가 편해진다.
   - 접근성이 우수해진다.
   - 시멘틱 웹 (시멘틱 태그가 모여 의미와 구조를 가진 거대한 데이터베이스)를 구성할 수 있다.




​     

