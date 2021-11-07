# vue.js 입문

참고문서

- 개발자의 품격 유튜브 : https://www.youtube.com/watch?v=sqH0u8wN4Rs

- 공식문서 : https://kr.vuejs.org/v2/guide/instance.html

  

## vue-lifecycle

![The Vue Instance Lifecycle](https://kr.vuejs.org/images/lifecycle.png)

- berforeCreated

  Vue 인스턴스가 초기화 된 직후에 발생됩니다. 컴포넌트가 DOM에 추가되기도 전이어서 `this.$el`에 접근할 수 없습니다. 또한 data, event, watcher에도 접근하기 전이라 `data, methods`에도 접근할 수 없습니다.

- created

   `data`를 반응형으로 추적할 수 있게 되며 `computed, methods, watch` 등이 활성화되어 접근이 가능하게 됩니다. 하지만 아직까지 DOM에는 추가되지 않은 상태입니다.

   cf). el 옵션은 Vue 인스턴스에 연결할 HTML DOM 요소를 지정한다.

- beforeMount

  가상 DOM이 생성되어 있으나 실제 DOM에 부착되지는 않은 상태입니다.

- mounted

  가상 DOM의 내용이 실제 DOM에 부착되고 난 이후에 실행되므로, `this.$el`을 비롯한 `data, computed, methods, watch` 등 모든 요소에 접근이 가능합니다.

  또한, 부모 컴포넌트의 mounted훅은 항상 자식 컴포넌트의 mounted훅 이후에 발생한다는 것을 알 수 있습니다.


- beforeUpdated

  변할 값을 이용해 가상 DOM을 렌더링하기 전이지만, 이 값을 이용해 작업할 수는 있습니다.

- updated

  약 변경된 값들을 DOM을 이용해 접근하고 싶다면, updated훅이 가장 적절합니다.

- beforeDestroy

  해당 인스턴스가 해체되기 직전에 **beforeDestroy**훅이 호출됩니다. 아직 해체되기 이전이므로, 인스턴스는 완전하게 작동하기 때문에 모든 속성에 접근이 가능합니다. 이 단계에서는 이벤트 리스너를 해제하는 등 인스턴스가 사라지기 전에 해야할 일들을 처리하면 됩니다.

- destroyed

  인스턴스가 해체되고 난 직후에 **destroyed**훅이 호출됩니다. 해체가 끝난 이후기 때문에, 인스턴스의 속성에 접근할 수 없습니다. 또한 하위 Vue 인스턴스 역시 삭제됩니다

