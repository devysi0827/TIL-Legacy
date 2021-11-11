# unity: webgl web 키 입력방지

### 문제

-  webgl을 웹에서 업로드한 후, 웹에서 타이핑을 해야할 때 생기는 문제

  - wasd 등 영타가 글을 칠 수 없고 유니티상 명령어로 입력됌

  

### 해결

1. TestWeb C#Script를 아래 코드를 추가해서 준비하기

```c#
void Webglstart()
    {
        WebGLInput.captureAllKeyboardInput = true;
    }

    void Webglend()
    {
        WebGLInput.captureAllKeyboardInput = false;
    }
```

 - 이 코드는 유니티로의 입력을 금지하고 따라서, 다시 영타가 쳐진다 (true= unity, false= web)



cf). 통신에서 설명했듯이 web에서 해당함수를 실행하면 된다.

cf2). 만약 webGLInput이 없는 변수로 취급된다면 file > build setting > webgl >switch flatform 을 순서대로 실행해서 flatform을 webgl로 맞춰주면 된다.

