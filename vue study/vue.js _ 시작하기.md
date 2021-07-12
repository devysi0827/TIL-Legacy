# vue.js 입문

참고문서

- 개발자의 품격 유튜브 : https://www.youtube.com/watch?v=sqH0u8wN4Rs
-  공식문서 : https://developer.mozilla.org/ko/docs/Web/Web_Components
- 나무위키 



## VUE.JS란?

- 컴포넌트 기반의 SPA를 구축할 수 있게 해주는 프레임워크

  - 컴포넌트 : 웹 컴포넌트는 그 기능을 나머지 코드로부터 `캡슐화`하여 재사용 가능한 커스텀 엘리먼트를 생성하고 웹 앱에서 활용할 수 있도록 해주는 다양한 기술들의 모음입니다.

    => 재사용이 좋다
    
    
  
- SPA : Single Page Application
  
  - 하나의 페이지 내부에서 필요한 영역 부분만 로딩 되는 형태
  - 빠르고, 트래픽(웹 사이트 방문자들이 주고받은 데이터 ) 양이 적다



- routeing이란?
  - 웹페이지간의 이동방법을 의미한다
  - 페이지 이동시, 서버에 요청하여 새로 갱신하는 것이 아니라 미리 해당 페이지를 받아 놓고 클라이언트의 라우팅을 이용하여 화면을 갱신함, 이러한 방식을 SPA라고 한다.
  -  뷰,리액트,앵귤러 모두 라우팅을 이용하여 화면을 전환함.



## VUE 들어가기

- vue 파일 생성하기

```
vue create `폴더명`
```

- vue-bootstarp 설치

```
npm install vue bootstrap bootstrap-vue
```

```js
// main. js 에 추가

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
```

- vue-router 적용하기
  - index.js
  
    ```js
    import Vue from "vue";
    import VueRouter from "vue-router";
    
    //app들 불러오기
    //import Home from "../views/Home";
    //import About from "../views/About";
    
    Vue.use(VueRouter)
    
    const router = new VueRouter({
        mode: "history",
        routes: [
            {path:"/", component: Home},
            {path:"/About", component: About},
        ]
    })
    
    export default router	
    ```
  
  - main.js
  
    ```js
    import router from "./router" //경로대로
    
    new Vue({
      router, // 이 부분 추가
      render: h => h(App),
    }).$mount('#app')
    
    ```
  
    

## vue syntax

- v-show vs v-if 

  둘 다 조건부 렌더링이나 v-show는 렌더링 후 표기여부를 v-if는 표기여부에 따라 렌더링을 결정한다.



- v-for

  ```html
   <option :key="i" :value="d.v" v-for="(d,i) in options">{{d.t}}</option>
  ```

  고유 key 속성이 반드시 필요, 보통 index 값을 사용

  d = 반복해서 가져오는 배열의 원소들, i = 그 원소들의 index

  

- v-on(@)

  이벤트리스너의 역활로 특정이벤트 발생 시 사용

  

- v-bind(:)

  vue의 상태데이터를 html 요소의 속성에 할당

  - filter를 적용가능
    - |로 사용하며 체이닝이 가능

  

- v-model

  html 요소값과 data를 양방향 바인딩

  

- watch vs computed

  - computed : 특정 값이 변동하면, 그 값과 연관된 값을 재계산하여 보여준다
    - 선언형 프로그래밍 : 계산 목표가 정의됌
  - watch : 특정 값이 변동하면 다른 작업을 실행시킨다
    - 명령형 프로그래밍 : 데이터가 바뀌면 특정 함수를 실행함



- lodash : js 라이브러리로 정렬, 랜덤 등 다양한 유틸 함수 제공

