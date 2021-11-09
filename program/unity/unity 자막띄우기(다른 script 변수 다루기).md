# unity: 자막 띄우기

문서를 전체 화면으로 보는 걸 권장합니다.

*타 컴포넌트의 변수를 다루는 법도 다루고 있습니다*

- unity 구조 : Wall과 GameManager을 사용합니다

![image-20211102152017739](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102152017739.png)



### 생성하기(사전준비)

1. Hierarchy > 마우스 오른쪽> ui > text or image 시 자막으로 사용가능한 물체들이 생성됌
2. Hierarchy > 마우스 오른쪽>Create Empty를 이용하여 GameManager란 빈 오브젝트 생성
3. Project > 마우스 오른쪽 > create > c# script GameManager란 script 생성(아이콘 톱니모양으로 자동으로 바뀜)

![image-20211102153745609](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102153745609.png)



### code : code를 먼저 작성해야 공간이 생김

- GameManager.cs

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameManager : MonoBehaviour
{	
    // 변수 talk 선언, gameobject 선언
    public bool talk;
    public GameObject TalkUi1;

    void Start()
    {
        // 초기값 설정
        talk = false;
    }

    // Update is called once per frame
    void Update()
    {
      // talk가 변하면 ui를 띄운다. 
      if (talk == false)
        {
            TalkUi1.SetActive(false);
        }

      if (talk == true)
        {
            TalkUi1.SetActive(true);
         }
    }
}

```



- wallCollider 수정

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WallCollider : MonoBehaviour
{
    // GameManager란 GameObject를 설정
    public GameObject GameManager;
    Renderer myRenderer;

    void Start()
    {
        myRenderer = GetComponent<Renderer>();
    }
    
    // Update is called once per frame
    void Update()
    {
        // space를 누른다면 작동
        if(Input.GetKeyDown(KeyCode.Space))
        {
            // gameManagerobject내부에 GameManager script component를 가져와서 거기 talk 속성의 접근
            GameManager.GetComponent<GameManager>().talk = false;
        }

        if (Input.GetKeyDown(KeyCode.G))
        {
            // <>안 스크립트 
            GameManager.GetComponent<GameManager>().talk = true;
        }
    }

    void OnTriggerStay(Collider other)
    {
        myRenderer.material.color = Color.red;
    }

    void OnTriggerExit(Collider other)
    {
        myRenderer.material.color = Color.white;
    }

}

```



### inspector 적용하기

1. TalkUi1의 설정을 해제 -> 게임에서 평상시 안보이게 됌

   - 그 외 기타 설정들 폰트나 위치등은 scene에서 맞추길 바람

   ![image-20211102155339973](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102155339973.png)

   

2. gameManager Object에 GameManager script를 할당

3. talk Ui1 칸에 TalkUI1을 드래그 & 드롭

   ![image-20211102161803853](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102161803853.png)



### 예시

![image-20211102162011668](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102162011668.png)