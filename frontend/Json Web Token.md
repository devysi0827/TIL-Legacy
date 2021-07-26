# Json Web Token



### JWT의 사용이유

1. 보안 이슈: 사용자가 로그인 하게 되면, 서버는 JWT를 리턴합니다. token을 인증 값으로 사용하게 되면 기존 쿠키/세션을 사용하는 방식보다 많은 보안 이슈를 막을 수 있습니다. 서버는 GUI로부터 받은 JWT가 유효할 경우, resouce를 사용하도록 허용합니다. 또한 JWT는 쿠키를 사용하지 않기 때문에, Cross-Origin Resource Sharing (CORS) 이슈가 발생하지 않습니다.
2. 데이터 용량: JWT는 기존의 XML보다 덜 복잡하고 인코딩 된 사이즈가 작습니다. 따라서 HTTP와 HTML 환경에서 사용하기 좋습니다.
3. 사용성: JSON parser는 대부분의 프로그래밍이 지원하기 때문에 XML을 사용하는 SAML 보다 만들기 쉽습니다.



### 과정 요약

1. loginpage에서 이메일과 비밀번호를 변수에 담아서 특정 함수(john ann __actions 등)나 백엔드에 보낸다

2. 백엔드에서 서버에 정보와 일치하면 `ok` 응답을 보내준다. (`프론트가 할 일 아님`)

3. `ok`응답이 있다면, web token을 cookie나 local storage에 저장하고 메인페이지로 이동한다.

   에러나 에러응답이 온다면, 경고문을 띄운다.

4. 토큰이 있다면, 로그인 상태로 확인한다(app.js에서 확인함)

   

### 코드참고블로그

https://im-developer.tistory.com/169

https://not-tasty-mango-soba.tistory.com/22



### vue code, sellyeji project

login.vue

```vue
<template>
  <div style="background-color: #F3EFE4;">
      <div class="textbox">
        <label for="username">사용자 이름</label>
        <input type="text" id="username" v-model="credentials.username">
      </div>
      <div class="textbox">
        <label for="password">비밀번호</label>
        <input type="password" id="password" v-model="credentials.password">
      </div>
      <button @click="login" class="btn btn-success">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'Maindoor' })
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
}
</script>

<style>
</style>
```



signup.vue

```vue
<template>
  <div style="background-color: #F3EFE4">
    <h1>Signup</h1>

    <div class="textbox">
      <label for="username">사용자 이름</label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
      
    <div class="textbox">
      <label for="password">비밀번호</label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
      
    <div class="textbox">
      <label for="passwordConfirmation">비밀번호 확인</label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
    </div>
      
    <div class="textbox">
      <label for="email">e-mail</label>
      <input v-model="credentials.email" type="text">
    </div>
 
    <button @click="signup(credentials)" class="btn btn-success">회원가입</button>

    
  </div>
  
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
        email: null,
      }
    }
  },
    
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}

</script>
```

