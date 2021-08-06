# react: npx create-react-app

### 개념

```
npx create-react-app [project_name]
```

원하는 react 초기설정 앱을 만들 수 있다.



### 내부 설명

- registerServiceWorker : 브라우저 서비스워커기능을 사용하기 위한 파일

- ```react
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
    document.getElementById('root')
  );
  ```

  - 문서에서 특정 아이디를 가지고 있는 dom을 가져와서 react component를 표시하겠다.
  - 이 경우에는 Dom에 'root' 위치에 App 컴포넌트를 표시하겠다가 됌
  - public 폴더에 dom에 해당하는 index.html이 존재한다

- package.json

  - 여러 설정파일들, 추가 설치파일들을 보여준다
  - npm eject로 기본설정파일들도 확인 가능하나 굳이 권장하지 않는다



### 자동완성

reactjs code snippet 설치

함수형: rfce + tab

화살표함수형: rsc +tab

class형: rcc + tab

