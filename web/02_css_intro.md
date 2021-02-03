# TIL 0201

## css

1. css(Cascading  Style  Sheets)
   - 레이아웃과 스타일을 정의하는 언어
   - HTML 구조를 그대로 두고 전혀 다른 레이아웃을 만들 수 있다.
   - HTML과 문법이 약간 다르다.



2. 이름 규칙

   - 이름은 포괄적으로 짓는다. 
     - brown_ BOX (X), dark_ box(o)



3. 자주 쓰는 문법

   - 항상 공식 문서를 참조한다

   https://developer.mozilla.org/ko/docs/Web/CSS/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/%ED%85%8D%EC%8A%A4%ED%8A%B8_%EC%8A%A4%ED%83%80%EC%9D%BC

   

   - ```html
    html에서 불러오고, <div class="container"> 식으로 부분적용하여 사용한다.
     ```
   
   
   
- 박스 생성 관련 문법
  
  - width, height : 700px;  너비, 높이를 700px로
     - border-width: 2px; 두께 조절
     - border-style: dashed; 점선으로
     - background-color : red; 박스색을 빨강으로

     

   - 박스 이동 관련 문법  

     - position : absolute; 박스 위치 절대설정

       - absolute : 상위 박스를 기준으로 위치를 정한다(없을시 최상위 body)
    - relative : 현재 위치를 기준으로 정한다
  
  - top, left, right, bottom: 50px 기준과 거리 설정 
  
    - 안쪽이 +이다.
  
     - margin: 0; 박스 와 홈페이지 끝 간격 조절
  
  - padding: 0; 박스와 박스 내부글 간격 조절
  
     - line-height: 35px; 줄간격을 조절한다. 조절하면, 수직정렬도 할 수 있다.

     - display: inline; 설정을 인라인으로 변경 

       
  
     

   - 글씨 관련 문법

     - font-family: Arial, Helvetica, sans-serif; 글씨체변경
     - font-size: 20px; 글씨 크기를 20으로
     - font-weight: bold 굵은 글씨
   - color: black; 글씨색 조절
     - text-align: center; 내용을 중앙으로 정렬
     - vertical-align: text-top; (수직정렬이라 하지만), 기준을 맞추어 요소들을 수평정렬한다.
  
     
  




​     







※ 참고하면 좋은 사이트 : https://flexboxfroggy.com/#ko