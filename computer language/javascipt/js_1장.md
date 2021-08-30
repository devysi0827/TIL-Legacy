#  Java Script: create, read



## 1. 기본양식

```html
......생략......

<body>
  <h1>todoapp</h1>

  <form>
  </form>

  <script> 
  </script>

</body>

</html>
```

- 기본형식 그대로에 form, script, h1만 작성한 상태이다
- 명세에 따라 form 태그를 사용하지만, 편의와 기능에 따라 div등 다른 태그 사용이 가능하다.



## 2. body 만들기

```html
<body>
  <h1>todoapp</h1>
  
  <form>
    <input id="todoinput" type="text">
    <button id="todobtn">submit</button>
  </form>

  <ul id="todolist">
    <li>목록1</li>
    <li>목록2</li>
  </ul>

  <script> 
  </script>
```

- ul > li*2로 한번에 만들 수 있다.
- form과 ul태그에서 각각의 태그를 사용하기 위해서 필요한 모든 항에 id값을 부여하였다.



## 3. Create 작성

```html
 <script> 
    function addlist(event) {
      event.preventDefault()
      // 1. input 태그 선택
      const inputtag = document.querySelector('#todoinput')
      // 2. 선택한 input의 value 값을 잡는다.
      const inputData = inputtag.value
      // 3. if문으로 빈칸 방지
      if (inputData){
        // 4. 새로운 li 태그 생성
        const liTag = document.createElement('li')
        // 5. 4에서 만든 태그의 innerText를 2번 value로 설정
        liTag.innerText = inputData
        // 6. 기존 ul 태그 선택
        const ulTag = document.querySelector('#todolist')
        // 7. 4에서 만든 li 태그를 5에서 만든 ul태그의 자식으로 추가(이때부터 문서에서 li가 보임)
        ulTag.appendChild(liTag)
        // 8. input 태그 내용을 지운다.(입력창에 입력한 내용 비우기!)
        inputtag.value = ""
      }
    }

    const addTodoBtn = document.querySelector('#todobtn')
    // addTodoBtn 을 'click' 하면, addTodo 함수를 실행하도록 설정한다.
    addTodoBtn.addEventListener('click', addlist)
  </script>
```



- 함수 선언

  ```html
  function function_name (event) {
      logic
  	return
      }
  ```

  - function == def(함수정의),  event =인자로 받아들이는 이벤트,  function_name= 함수명

  - 함수, fuction_name은 받은 event에 대해서 logic을 수행한 뒤 그 결과를 return한다.
  
    

- event.preventDefault()

  - `html` 에서 `a` 태그나 `submit` 태그는 고유의 동작이 있다. 페이지를 이동시킨다거나 `form` 안에 있는 `input` 등을 전송한다던가 그러한 동작이 있는데 `e.preventDefault` 는 그 동작을 중단시킨다.

    => 페이지의 갱신을 막고, 수정이 가능하다.



- const

  - 변수 const를 이용해서 inputtag, inputdata, litag 등 변수명 선언
  
  - queryselector를 이용해서 id(`#todoinput`)나 태그를 통해서 원하는 태그를 변수에 대입할 수 있다.

  - 변수 let과 var가 더 있는데 원한다면 더 찾아볼 것.
  
    
  
- if문

  ```
  if (condition) {
          logic
      }
  ```

  - 위와 같은 양식을 통해서, python처럼 if문 사용이 가능합니다.

  - 내부 logic은 자바스크립트 문법을 따릅니다.

  

- createElement
  - 자바스크립트를 이용하여 문서에 HTML 요소를 추가할 수 있습니다. 
  
  - 이 과정만으로는 문서에 표시되지 않습니다.
  
    

- SelcetNode  .appendChild(childNode)
  - 선택 노드에 자식 노드를 추가합니다.
  - 위에 생성한 요소들은 `body`나 그 이하 태그들에 추가함으로써 문서에 보이게 할 수 있습니다.



- 함수 사용법

  ```html
  변수명.addEventListener('event', 함수명)
  ```

  - `변수`가 `event`에 의해서 발생하면 `함수`를 실행시킨다.

  

  