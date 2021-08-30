1. html

   hyper text markup language

   what is hyper text?

   http html



2. html 구조

   - html : 최상위요소이자 문서의 root head와 body로 나누어진다.
   - head :  문서 제목,  문자 코드 css선언 외부파일 로딩 등 브라우저에 나타나지 않는 정보를 기록
   - body :  브라우저에 나타나는 내용들

   

3. 태그

   - 태그별로 기능이 다르다
   - 닫는 것과 여는 것이 반드시 필요하다.

   

5. 시멘틱 태그

   - 의미와 구조를 담은 태그가 등장, 실제로 div, span과 다를 바가 없다.
   - h1과 table도 시멘틱 태그로 볼 수 있다
   - 검색엔진최적화를 위해서 메타태그 시멘틱태그 등 마크업을 효과적으로 할 필요가 없다

   - header :  머릿말

   - nav :네비게이션

   - aside : 사이드에 위치한 공간: 메인컨텐츠와 관련성이 적음

   - section : 문서의 일반적은 구분 컨텐츠이 그룹 표현

   - article : 문서 페이지 사이트 안에서 독립적으로 구분되는 영역

   - footer: 문서전체나 섹션의 마지막 부분

6.  시맨틱 웹

   - 시맨틱 태그들이 모여서 메타데이터가 의미를 가진 웹페이지, 웹페이지들이 의미와 관련성을 지닌 거대한 데이터베이스로 구축되었다.

7.  인라인 & 블록

   - block: 

     - 줄 바꿈이 일어나는 요소, 가로폭 전체를 차지, 인라인 요소만 블록안에 들어갈 수 있다.

     - div, ul, ol, li, p, hr, form

   - inline:

     - 줄바꿈이 없는 행의 요소, 컨텐트 크기만큼, width, height,margine-top,bottom 지정 불가능

     - 상하 여백은 line-height로만 가능
     - span, a, img, input, label, b, em, i, strong

   - inline-block :

     - 블록과 인라인 레벨 특징을 모두가짐
     - 한 줄 표시도 가능하지만 width, height,margin도 설정가능하다

   - dispaly: none

     - 화면에 표시하지 않고 공간도 사라진다
     - visibillity : hidden은 공간은 차지하나 화면표시를 안한다

8. 그룹 컨텐츠

   ```
   <p> 
   <hr> 헤드라인
   <ol>
   <ul>
   <pre>
   <blockquote>
   <div>
   ```

9. 텍스트 요소

   ```
   <a> 
   <b> or <strong> 뒤는 의미가 불음
   <i> or <em>
   <span> <br> <img> 줄바꿈 이미지
   기타등등
   ```

10. table

    ```
    <tr>
    <td>
    <th>
    <thread>
    <tbody>
    <tfoot>
    <caption>
    셀 병합 속성 : colspan, rowspan
    scope 속성
    <col>, <colgroup>
    ```

11. form

    ```
    form은 서버에서 처리될 데이터를 제공
    action 
    method
    ```

12. input

    ```
    다양한 타입을 가지는 입력 데이터 필드
    label: 서식 입력 요소의 캡션
    name
    placeholder
    required
    autofocus
    ```

13. cascading style sheets

    - 스타일 과 레이아웃을 통해 HTML을 표시하는 방법을 지정하는 언어

    ```
    - 색상
    color
    font-size
    - text
    변형 서체
    background-image, color
    ```

    - 선택자, 속성, 값, 선언
    - 인라인(그 내부에 따로 style 선언) , 내부참조(style), 외부참조(link file)로 정의한다

13. 선택자

    - HTML 문서에서 특정한 요소를 스타일링 하기 위해서 필요하다
    - 기본선택자 : 전체, 요소, 클래스, 아이디, 속성 선택자
    - 결합자 : 자손 결합자, 자식 결합자 

      

15. 중요도 우선순위

    - !important >인라인> id선택자>class 선택자> 요소 선택자> 소스 순서

    (quiz 코드)

16.  css 상속

    - 상속되는 것 text 요소
    - 상속되지 않는 것 position and box 모델 등

17. css 단위(상대 크기 단위)

    - px(디바이스 상대단위), %(전체 브라우저 크기 대비), em(부모 대비 퍼센트), rem)오직 html기준), viewport(뷰포트 배율) 단위(vw, vh, vmin, vmax)
    - em ,rem 차이

17. box model

    - margin : 최외각 테두리
      - top, right, bottom, left로 조절
      - 1: 전부 2: 위, 아래 : 첫번째, 양옆 : 두번째 3: 위: 첫 양옆:두번째 아래: 세번째 4:위오아왼(시계방향)
      - 인접영역 마진은 중복된다(50 70이면 120이 아닌 총 70만 떨어진다)
    - border : 테두리 영역(마진과 패딩 사이)
    - padding : 가장 내부 테두리 여백
    - content : 글이나 이미지 내용
    - border-width : 점섬 두께
    - border-style : 점선
    - border-color : 점선 색

    $ 너비를 100으로 하면 마진을 제외한 실제 박스 길이는 몇인가?

    너비+패딩+보더길이

    $content-box와 border-box의 차이는?

    border box --> content +margin =이 width

    content box --> content만 width

18. css position:
    - static: 디폴트값(기준 위치, 좌측 상단, 부모요소 내 배치도리 경우 부모 요소의 위치를 기준으로 배치된다.)
    - top, bottom, left,right로 이동
    - relative: static 위치 상대이동
    - absolute: 부모 기준 절대위치로 이동
    - fixed 브라우저 기준 항상 같은 위치로 이동 후 고정

19. 강의

    - viewport : 화면에 대한것

      '* ' 전체 선택자

      .box > p box 선택자 바로 아래 자식 p에대해서만

      .box p : box 내부 모든 자손 p에 대해서

      id는 문서당 한번만 사용

      blue green green blue -> 우선순위가 같아서 소스순위로 넘어감

      rgba(a=투명도)

       hsl= 색창 채도 명도

      margin 0 outo( 두번째 outo를 자동정렬 시킴)

      블록 -> 마진으로 정렬, 텍스 트 -> tetxt-align으로 정렬