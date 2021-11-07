# unity: 캐릭터 움직이기

전체 화면으로 보는 걸 권장합니다.

캐릭터는 움직이지만, 애니메이션 효과를 적용하지 않기에 추가적인 공부가 필요합니다

- unity 구조

![image-20211102152017739](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102152017739.png)



### inspector 적용하기

1. addComponent로 Rigidbody를 추가

   - why? rigidbody를 설정하면 중력을 받고 물리법칙이 작용하는 현실물체가 됌

     

2. 불필요한 회전 제한

   - RIgidbody 내부에 Constraints를 이용하여 특정방향의 회전 또는 물체의 이동을 막을 수 있음.

   

3. addComponent로 script를 추가

   - script code를 통해 명령을 할 수 있음 

     ex). 왼쪽키를 누르면 왼쪽으로 움직여, g키를 누르면 대사창을 띄워, a키를 누르면 재시작해 등

![image-20211102151716531](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102151716531.png)





### code

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerCube : MonoBehaviour
{
    // speed 설정
    public float speed = 10f;
    // 강체 설정 (=player)
    Rigidbody playerRigidbody;

    void Start()
    {	
        // playerRigidbody = rigidbody에서 가져옴
        playerRigidbody = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        // 속도값 변수 설정 GextAxis는 해당 축의 이동 정도를 -1~1로 가져옴
        // Horizontal은 예약어로 키보드 왼쪽키, 오른쪽키의 눌림, vertical도 동일
        float inputX = Input.GetAxis("Horizontal");
        float inputZ = Input.GetAxis("Vertical");
        // 중력 정상화를 위한 추가코드
        float fallSpeed = playerRigidbody.velocity.y;
        // 속도벡터를 아래와 같이 적용함 
        Vector3 velocity = new Vector3(inputX, 0, inputZ);
        // 속도배율을 적용
        velocity = velocity * speed;
        // 위에 적용한 중력 정상화 진행
        velocity.y = fallSpeed;
        // 강체에 속도를 적용
        playerRigidbody.velocity = velocity;


    }
}

```

