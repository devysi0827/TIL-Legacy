# spring _ 김영한 _ 스프링입문 _ 5강

### 정적컨텐츠

- 파일 그대로를 사용



### 정적컨텐츠 탐색 과정

<img src="spring _ 김영한 _ 스프링입문 _ 5강.assets/32.png" />

1. 웹 브라우저에서 요청을 보냄
2. `controller`가 존재하는지 스프링에서 탐색
3. 관련 컨트롤러가 없다면, resources에 있는지 확인하고 있다면 그걸 렌더링



### mvc와 템플릿 엔진

mvc : model, view, controller

```java
   @GetMapping("hello-mvc")
    public String helloMVC(@RequestParam("name") String name, Model model) {
        model.addAttribute("name", name);
        return "hello-template";
    }}
```

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Hello</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
<p th:text="'hello' + ${name}" ></p>
</body>
</html>
```

<img src="spring _ 김영한 _ 스프링입문 _ 5강.assets/mvc.png"/>

- http://localhost:8080/hello-mvc?name=devysi 등으로 하여 ? 뒤에 변수값을 넣어줄 수 있다.
- viewResolver에서 위에서 받은 모델, 변수 등에 맞는 처리를 변환하여 웹으로 넘겨준다.



cf). 에러가 난다면 log를 읽자

cf2). ctrl + p로 자바의 속성값을 볼 수 있다 (required 등을 살펴볼 때 좋다.)



### API

```java
@GetMapping("hello-string")
    @ResponseBody
// http response의 body에 직접 넣어주겠다.
    public String helloString(@RequestParam("name") String name) {
//        model.addAttribute("name", name);
        return "hello" + name;
    }
```

- 위 템플릿엔진과의 차이점 : 소스보기 시 code가 아닌 `hello name`만 나옴
  - mvc 템플릿엔진은 코드를 수정한다음 나에게 보여준 것
  - API는 정보만 전달하는 것



```java
@GetMapping("hello-api")
@ResponseBody
public Hello helloApi(@RequestParam("name") String name) {
    Hello hello = new Hello();
    hello.setName(name);
    return hello;
}
static class Hello {
    private String name;
    private  String height;
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }

    public String getHeight() {
        return height;
    }
    public void setHeight(String height) {
        this.height = height;
    }
}
```

- Hello hello = new Hello();

  - Hello 클래스의 hello 변수는 새로운 Hello 객체

- 이렇게 보낼경우 화면에 {"name":"내가 param으로 보낸 값"} 즉, json으로 전달된다.

  <img src="spring _ 김영한 _ 스프링입문 _ 5강.assets/api.png"/>

  

  1. hello-api 요청 -> hellocontroller 연결
  2. `@ResponseBody`를 보고 그대로 데이터를 넘기도록 동작
  3. 하지만, 문자가 아닌 객체이기때문에 json으로 바꿔서(jsonConverter) 전달해줌

  

  

  

  cf). alt + insert : getter, setter 단축키

