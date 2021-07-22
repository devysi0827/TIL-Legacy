# react import require

### require

- 남이 만든 js 또는 내가 만든 js를 불러와서 사용할 수 있다. (import와 동일)

- node 문법으로 react, webpack, js 등 모든 부분에서 사용 가능하다

- export default로 한 값을 default로 불러오게된다.

  - 아래의 코드의 경우 변수명 React는 해당 javascript 문서에서 쓰는 명이고 불러온 것은 react.js에 default값이다 
  - default 값은 js문서당 하나만 존재할 수 있다.

  ```javascript
  const React = require('react')
  ```

  - 반대로, 다음에 오는 코드처럼 {}로 감싸진 코드들은 export `변수명`으로 따로 지정해준 케이스들을 불러올 때 사용하며 변수명이 다르다면 여러개 있어도 괜찮다

  ```
  const { useState,useRef } = React 
  ```

  

### import

- 남이 만든 js 또는 내가 만든 js를 불러와서 사용할 수 있다. (require와 동일)

- webpack이 지원해줘서 대부분에 react에서 호환되나, webpack 문서에서는 사용이 불가능하다.

  



