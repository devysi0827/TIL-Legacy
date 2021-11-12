# unity: webgl web과 통신하기(1)

- webgl unity를 web에 무사히 업로드 한 후를 다루고 있습니다.

- unity에서 web(html)과 통신하는 법을 다룹니다
- 아래는 폴더 구조입니다.

![image-20211110001939685](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211110001939685.png)



### 웹과 통신하기

1. TestWeb C#Script를 아래 코드로 준비하기

```c#
using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using UnityEngine.Networking;


public class TestWeb : MonoBehaviour
{
 	void Start()
    {
        // 이로 인해서 버튼을 클릭시, Example 함수가 실행됨
        GameObject.Find("GetButton").GetComponent<Button>().onClick.AddListener(Example);
    }


    void Example()
    {
    	// 1항: web에서 실행시킬 함수의 이름, 2항: 전달할 변수값
        Application.ExternalCall("MyFunction", "Hello from Unity!");
    }
}
```

2. TestWeb을 임의의 GameObject에 배치하기
   - 저는 Getbutton이라는 함수에 TestWeb이 들어있는 걸 맨 위 사진 insepector에서 확인할 수 있습니다.
3. webgl build 후 vue에 배치(전 글 참조)
