# unity: WEBGL 빌드 하기

문서를 전체 화면으로 보는 걸 권장합니다.



### 빌드하기

1. 상단 네브바 > file > build setting
2. webgl click 후 switch

![image-20211102162654711](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102162654711.png)

3. player setting > webgl에서 아래 설정과 동일한지 확인 (아마 동일)

![image-20211102162757898](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102162757898.png)

![image-20211102162827349](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102162827349.png)

4. 설정이 완료되면 build 버튼을 눌러서 빈 폴더를 만들고 build , 이때 폴더명이 중요함!!!

   ![image-20211102162945104](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102162945104.png)

5. build한 파일을 들어가서 제대로 build 되었나 확인 



### vue에 적용하기

1. vue-unity-webgl 설치

   https://github.com/votetake/vue-unity-webgl
   
2. 폴더 구조 맞추기

   - 반드시 public안에 unity 폴더를 넣어야함 이 unity 폴더는 위에서 빌드한 파일들이 들어있음
   - unity란 폴더이름은 중요하지 않음 

   ![image-20211102163822617](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211102163822617.png)

3. public 바로 아래 index.html에 아래 코드 추가

   ```
   <script src="unity/Build/UnityLoader.js"></script>
   ```

4.  code 작성

```vue

<template>
<--- unity tag에 기본경로가 public으로 잡혀있기 때문에 ./ 하고 바로 이어나가면 된다.--></--->
<div id=app>
  <unity 
  src="./unity/Build/build.json" 
  width="1000" 
  height="600" 
  unityLoader="./unity/Build/UnityLoader.js"
  >
  </unity>
</div>  
</template>



<script>
import Unity from 'vue-unity-webgl'

export default {
  name: 'App',
  components: {
    Unity
  }
}
</script>

<style>
</style>

```

