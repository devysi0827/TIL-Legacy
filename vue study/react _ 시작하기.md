# react 입문

참고문서

- [[무료\] 따라하며 배우는 노드, 리액트 시리즈 - 기본 강의 - 인프런 | 강의 (inflearn.com)](https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본#curriculum)



## 강의 방식 및 설치(1~)

- 보일러플레이트 :  변경없이 계속하여 재사용할 수 있는 저작품(프로그램) 제작

- node.js, express.js 설치 및 실행

  - npm init : package만 있는 파일 생성

  - index.js : backend 시작점 생성

  - express.js => node.js framework

    ```
    npm install express --save
    npm run start
    ```

    [Installing Express (expressjs.com)](http://expressjs.com/en/starter/installing.html)



- 몽고DB

  ```
  npm install mongoose --save
  
  ```

  - index.js

    ```js
    const mongoose = require('mongoose')
    mongoose.connect('mongodb+srv://devysi:tkatjd2508!!@boiler-plate.ezrrw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',{
        useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false
    }).then(()=> console.log('connect'))
    .catch(err => console.log(err))
    ```

    몽고 db 연결 후 npm run start로 확인

  - db만들기

    ```js
    // in user.js
    
    const mongoose = require('mongoose');
    
    const userSchema = mongoose.Schema({
        name: {
            type: String,
            maxlength: 50
        },
        email: {
            type:String,
            trim: true,
            unique:1
        },
        image: String,
        token: {
            type: String
        },
        tokenExp : {
            type:Number
        }
    
    })
    
    //model을 스키마로 감싸준다..?
    const User = mongoose.model('User',userSchema)
    
    // 모듈화하여 다른곳에서 사용
    module.exports = {User}
    ```

    

- git 설치하기 및 gitignore 설정 및 연결
  - SSH (Secure Sell) 설정은 pass 합니다



- body-parser(express 최신버전 이후 생략)
  - 특정 데이터를 저장하여서 요청과 같이 보냄



- nodemon 

  ````
  npm install nodemon --save-dev
  ````

  - 서버를 따로 끄거나 키지 않고 저장만으로 반영이 됌



- 비밀번호관리(헤로쿠(배포툴) OR dev)
  - key를 이용하여 배포시와 비배포시 db 접속경로를 구분
  - 개발환경에서 다루는 js파일을 gitignore에 등록



- bcrypt

  ```
  npm install bcrypt --save
  ```

  - 비밀번호 암호화 프로그램
  - https://www.npmjs.com/package/bcrypt



- jsonwebtoken

  ````
  npm install jsonwebtoken --save
  ````

  - token 생성 프로그램
