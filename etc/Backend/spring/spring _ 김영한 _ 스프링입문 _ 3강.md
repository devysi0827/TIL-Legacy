# spring _ 김영한 _ 스프링입문 _ 3강

### view(welcome page 만들기)



### index.html

- main > resources > static > index.html 생성

- spring에서 자동으로 welcome page로 연결해준다. (https://docs.spring.io/spring-boot/docs/current/reference/html/web.html#web)



### template engine

- https://www.thymeleaf.org/

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head>
<title>Hello</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
<p th:text="'안녕하세요. ' + ${data}" >안녕하세요. 손님</p>
</body>
</html>

```

- th : 타임리프 약자 첫줄 xmlns을 통해서 타임리프 문법을 사용할 수 있게 되었다.
- p tag text에는 안녕하세요 + {data} 가 출력된다.



### spring 진행구조

<img src="spring _ 김영한 _ 스프링입문 _ 3강.assets/123.png"/>

```java
@Controller
public class HelloController {
    @GetMapping("hello")
    public String hello(Model model) {
        model.addAttribute("data", "hello!!");
        return "hello";
    }
}
```

1. 웹브라우저에서 `localhost:8080/hello`라 전송 => 내장 톰캣 서버를 거쳐서 스프링에 전송
2. `@GetMapping("hello")`를 통해서 'hello' get요청에 대해서 해당 hello method가 실행됨.
3. spring에서 넘어온 model에 ("data", "hello!!")를 넣는다 
4. return hello (hello.html을 위 정보를 가지고 렌더링해라)
5. 이 리턴값을 `viewResolver`가 화면(html)을 찾아서 처리해준다.





cf). controller : 특정 로직을 맡아 처리하기 위한 중간제어자 로 역할분담을 통한 유지보수 기능 상향을 위해 쓴다.

cf2). spring boot devtools를 깔면 자동 컴파일이 된다.
