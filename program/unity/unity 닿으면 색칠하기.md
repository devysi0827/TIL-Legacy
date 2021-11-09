# unity: 색칠하기

문서를 전체 화면으로 보는 걸 권장합니다.

- unity 구조 : Wall을 사용합니다

![image-20211102152017739](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102152017739.png)



### inspector 적용하기

1. Component의 Box Collider > is Trigger를 체크(추가)

   - why? is trigger를 체크하지 않으면 충돌을 하는 물체지만, 체크를 하면 충돌하지 않고 이벤트 공간(충돌을 판별하는 공간)으로 사용가능

     

2. 그럼 충돌하면서 event도 인식하려면?

   - Box Collider를 하나 더 추가함 => 하나는 이벤트를 인식, 하나는 벽으로서의 역활

   

3. addComponent로 script를 추가

   - script code를 통해 명령을 할 수 있음 

     ex). 충돌시 색을 바꿔! 충돌이 끝나면 색을 원래대로 되돌려! 등

![image-20211102153225708](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102153225708.png)





### code

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WallCollider : MonoBehaviour
{
    // Start is called before the first frame update
    // renderer를 선언 instructor의 mash renderer를 의미
    Renderer myRenderer;

    void Start()
    {
        myRenderer = GetComponent<Renderer>();
    }
    
    // Update is called once per frame
    void Update()
    {
    }
	
    // OnTriggerStay: 이벤트 공간과 닿고 있거나 닿았으면 실행
    void OnTriggerStay(Collider other)
    {	
        // Color는 미리 대략적인 색을 모아둔 지시어
        // instructor > mash renderer > material > color = 빨강 으로 대입
        myRenderer.material.color = Color.red;
    }
	
    // OnTriggerExit: 이벤트 공간과 닿음이 해제되면 실행
    void OnTriggerExit(Collider other)
    {
        myRenderer.material.color = Color.white;
    }

}

```

