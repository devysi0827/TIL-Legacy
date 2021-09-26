# kakao link with vue

### index.html

```html
<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <title><%= htmlWebpackPlugin.options.title %></title>
    <script 
      src="https://developers.kakao.com/sdk/js/kakao.js"
      >
    
    </script>


    <script>
        // SDK를 초기화 합니다. 사용할 앱의 JavaScript 키를 설정해 주세요.
        Kakao.init("js key");

        // SDK 초기화 여부를 판단합니다.
        console.log(Kakao.isInitialized());
    </script>
  </head>
  <body>
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <div id="app"></div>
    <!-- built files will be auto injected -->
  </body>
</html>

```

- src="https://developers.kakao.com/sdk/js/kakao.js" 와 Kakao.init을 넣어주어야만 아래 함수들이 움직인다

  

### AboutPage.vue

```vue

<template>
  <div class="about">
    <button @click="KakaoRequest()">공유하기</button>
    
  </div>
</template>

<script>
export default {
  name: "about",
  methods : {
    KakaoRequest: function() {
      window.Kakao.Link.sendDefault({ 
        objectType: 'feed', 
        content: { 
          title: '나와 닮은 얼굴은????', 
          description: '지금 바로 나와 닮은 문화재를 찾아보세요!', 
          imageUrl: "https://ifh.cc/g/hoxmvR.png",
          // https://ifh.cc/i-C0zXn8
          link: { 
            mobileWebUrl: 'http://localhost:8080', 
            webUrl: 'http://localhost:8080', 
              }, 
            }, 
          buttons: [{ 
            title: '이리오너라!!', 
            link: { 
              mobileWebUrl: 'http://localhost:8080', 
              webUrl: 'http://localhost:8080', 
              },
            }], 
          }) 
        }, 
      }, 
    }


</script>

```

- 버튼을 누르면 해당공유하기 내용이 전달되는 코드를 구현하였다
- 코드내용 상세 설명
  1. window.Kakao.Link.sendDefault : 앞에 윈도우를 붙여야 webpage init을 제대로 사용할 수 있다.
  2. objectType: 보내는 양식 스타일을 선택가능하다
  3. content: 카카오 공유하기 중앙 내용을 구성한다, 이때 imgUrl은 http: 로 구성된 정보만 나온다
  4. buttons: 버튼의 내용과 링크를 정할 수 있다