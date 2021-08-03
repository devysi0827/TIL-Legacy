# react: virtual DOM

## Virtual Dom(VDOM)

### 개념

VDOM에 변화한 내용을 적용하고, 실제 DOM과 비교하여 변화한 부분만을 실제 DOM에 동기화하는 프로그래밍



### 왜 사용하는가?

"데이터가 바뀌면, mutation(변화)하지말고 view를 새로 만들자!" 라는 방식을 고려

이 방식을 사용한다면, 비약적으로 난이도가 쉬워진다(수정로직이 사라지기때문에)

하지만, 반대로 매 번 DOM을 갱신한다면, 시스템적인 부담도 엄청날 것이다.

**그래서 VDOM에 미리 적용하고, 실제 DOM과 비교하여 변화가 필요한 부분만을 찾아서 변경함으로써 시스템적인 부담을 줄인다 **



### 어떻게 비교하는가?

1. 서로 다른 타입의 두 엘리먼트는 서로 다른 트리를 만들어낸다.
2. 개발자가 `key` prop을 통해, 여러 렌더링 사이에서 어떤 자식 엘리먼트가 변경되지 않아야 할지 표시해 줄 수 있다.

key와 엘리먼트를 통해 비교하면 DOM과 VDOM을 매우 빠르게 비교할 수 있다.

 

## 참고링크

Virtual Dom 공식문서: https://ko.reactjs.org/docs/faq-internals.html

재조정 공식문서 : https://ko.reactjs.org/docs/reconciliation.html

Velopert : https://www.youtube.com/watch?v=wKwMRH0PkMg&list=PL9FpF_z-xR_E4rxYMMZx5cOpwaiwCzWUH&index=3
