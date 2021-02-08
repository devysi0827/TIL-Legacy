1. html의 풀네임을 쓰시오

   

   

2. html에서  문서 제목,  문자 코드 css선언 외부파일 로딩 등 브라우저에 나타나지 않는 정보를 기록하는 공간은  어디인가?

   

3. 다음 중 틀린 것은?

   ```
   1. <span>은 블락 요소이다.
   2. <h1>도 시멘틱 태그로 볼 수 있다.
   3. <img>는 닫는 태그가 없다.
   4. 시멘틱 태그 대신 <div>를 써도 웹페이지 상 문제는 없다.
   ```

   

   

4.  다음 중 틀린 것은?

   ```
   1. <form>은 대표적인 블록 요소이다.
   2. inline은 상하 여백을 line-height로만 정렬한다.
   3. 블록 안에는 인라인 요소가 들어갈 수 있다.
   4. inline은 margin-top을 설정할 수 있다.
   ```

    
   
5. 다음 중 옳은 것은?

```
1. <img>는 대표적 블락 요소이다
2. inline은 margin-left를 이용하여 여백을 만들어줄 수 있다.
3. <hr>은 단순 띄어쓰기의 의미를 가진다.
4. <ul>은 useful list의 약자로 번호를 붙이는 리스트들을 의미한다.
```



6. `<b>`와 `strong` 의 차이를 서술하시오.



7. 다음 중 틀린 것은?

   ```
   1. a는 대표적 인라인 요소이다.
   2. display: none을 사용하면 화면에 표시되지 않지만 공간은 유지한다.
   3. <i>를 사용하면 글자가 기울어진다.
   4. inline-block은 width를 설정할 수 있다.
   ```



8. css를 적용하는 세가지 방법과 그 차이점을 서술하시오



​	9. 중요도 우선순위를 알맞게 나열하시오

- 요소 선택자,  !important , 인라인, class 선택자, 소스 순서,  id선택자,



10. 다음 중 상속 되는 것은?

```
1. pont-size : 10px
2. margin: 10px
3. position :relative
4. back-groundcolor :red
```



11. 다음 코드를 보고 출력되는 '4'의 크기를 판단하시오.(글자의 기본사이즈는 16px이다.)

```html
 <style>
    .word{
      color: red;
      font-size: 1.5em;
    }
    .big{
      font-size: 1.5rem;
    }
  </style>

<body>
  <b class ="big">
    <b class ="big">4</b>
  </b>
</body>

```



12. 다음 코드의 결과 두 박스사이 마진은 몇인가?(단위 생략)

```html
<style>    
.top{
      margin-top: 70px;
 }
.bottom{
      margin-bottom: 30px;
}
  </style>
</head>
<body>
  <div class="box bottom" ></div>
  <div class="box top"></div>
</body>
</html>
```



13. 다음 스타일을 적용했다면 오른쪽 마진은 몇인가???

```
-1 :margin: 10px 20px
-2 :margin: 10px 20px 30px 40px
```



14. 컨텐츠의 길이를 쓰시오 (단위 생략)

    ```html
     <style>
     .box{
          background-color: rosybrown;
          width: 100px;
          height: 100px;
          padding-left: 1px;
          
        }
        .border{
          box-sizing: border-box;
        }
        
    
      </style>
    </head>
    <body>
      <div class="box border" ></div>
      <!-- <div class="box "></div> -->
    </body>
    </html>
    ```

15. box-sizing 에서 컨텐츠 박스와 보더 박스의 차이를 설명하시오



16. 다음 설명중 옳은 것은?

```
1. relative는 부모 위치 기준 상대이동을 한다.
2. box > p 는 박스 선택자 아래 모든 자손에 적용된다느 의미이다.
3. id는 html 파일에서 단 한번만 정의하고 사용할 수 있다.
4. maring: 0 auto를 사용하면 양쪽 마진값이 동일해진다
```



17. 다음을 출력했을 때 결과로 알맞은 것은?(위에서부터 1번, 4번은 error)

```html
<body>
  <div class="row" >
    <div class="col bg-primary">1 </div>
    <div class="col bg-secondary">2 </div>
    <div class="col bg-success">3 </div>
    <div class="col bg-info">4 </div>
    <div class="col bg-warning">5 </div>
  </div>
```



![KakaoTalk_20210207_220536173](web_study.assets/KakaoTalk_20210207_220536173.png)



18. mt - 1,2,3,4,5를 적용했을 때 떨어지는 마진은 각각 기준(16px)의 몇 배인가?



19. 다음 중 flexbox에 대하여 틀린 것은?

```
1. flex-direction:column을 적용하면 위에서부터 쌓이게 된다.
2. order는 숫자가 높을 수록 우선순위가 낮다.
3. flex-grow는 전체 공간을 비율에 맞게 나누어 준다. 
4. flexbox에서 self를 사용하면 컨테이너가 아닌 본인을 기준으로 정렬이 적용된다.
```



20. 이미지를 텍스트에 영향받지 않고 주위를 둘러서 뜨게 만드는 기능(class)의 이름을 쓰시오



21. 부트스트랩에서 왼쪽으로 패딩을 16px를 줄 때 사용하는 class를 쓰시오



22. flex-wrap과 display-flex가 적용되어 있을 때, 다음 개구리를 정렬하기 위해서 사용해야할 flex박스 명령어를 쓰시오.

```
align-content: flex-start
align-itmes :flex-start
justify-content :flex-start
justify-content :flex-end
```





![KakaoTalk_20210207_222908358](web_study.assets/KakaoTalk_20210207_222908358.png)



23. greed system에서 flex-direction: column은 어떻게 쓸 수 있는 지 명령어(class)를 쓰시오.

    



24. xs, sm, md, lg, xl의 범위를 쓰시오













````
답지:
1. hyper text markup language
2. head
3. 1
4. 4
5. 2
6. b는 단순한 굵음의 의미이지만, strong은 시멘틱태그처럼 의미를 강조한 것이다.
7.2
8. 인라인(그 내부에 따로<a style="".....>등으로 직접 선언) , 내부참조(head쪽에 style을 따로 사용), 외부참조(link file을 불러온다)로 정의한다
9. !important >인라인> id선택자>class 선택자> 요소 선택자> 소스 순서
10. 1
11. 24
12. 70
13. 20 20
14. 99
15. content는 content 길이만, border은 content+ padding의 길이
16. 4
17. 1
18. 0.25 0.5 1 1.5 3
19. 3
20. float
21. ms-3
22. 1
23. flex-column
24.576미만 576이상 768이상 992이상 1200이상 1400이상
````

