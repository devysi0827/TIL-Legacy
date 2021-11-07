# react: props

### props

부모 컴포넌트에서 자식 컴포넌트로 특정 값을 보내는 방법



```react
//App.js
import "./styles.css";
import Test from "./Test"

export default function App() {
  return <Test name="소영" />;
}

//Test.js
import React from "react";

const Test = ({ name }) => {
  return <div>내 이름은 {name}</div>;
};
Test.defaultProps = {
  name: "세일"
};

export default Test;
```

- 소영이란 값을 Test에 넣어서 보냄 => Test에서 소영값이 name으로 도착하여 사용됌
- 아무값도 안내릴 경우, default 값 설정가능(Test.defaultProps)



cf). 구조분해할당

javascript에서는 해당 변수에 할당하는 내용들을 찰떡같이, 분해해서 대응해준다.

위에서 사용되어서 변수가 완벽히 들어간 것

https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment

