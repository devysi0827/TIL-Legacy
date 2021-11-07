// express app 가져오기
const express = require('express')
// 새로운 express 앱 생성
const app = express()
// 포트 설정
const port = 5000
const bodyParser  = require('body-parser')
const {User} = require("../models/User")
const {auth} = require("./middleware/auth")
const cookieParser = require('cookie-parser')
const config =require('./config/key')

// json 파일과 다른 형태의 파일들을 해석할 수 있게 설정
app.use(bodyParser.urlencoded({extended: true}))
app.use(bodyParser.json())
app.use(cookieParser())

const mongoose = require('mongoose')
mongoose.connect(config.mongoURI,{
    useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false
}).then(()=> console.log('connect'))
.catch(err => console.log(err))

// 아래 함수를 실행
app.get('/', (req, res) => {
  res.send('Hello World! kkk')
})

app.get('/api/hello', (req,res) => res.send('hello world'))

app.post('/api/users/register',(req,res) =>{
    const user = new User(req.body)

    user.save((err, userInfo) =>{
        if (err) return res.json({success:false, err})
        return res.status(200).json({
            success:true
        })
    })
})

app.post('/api/users/login',(req,res) =>{
  //이메일이 있는가? mongodb method 사용 --> findone은 인터넷에서 제공하는  함수입니다!!!!!!!!
  // db에서 해당 이메일에 대항 정보를 가져옴 
  User.findOne({email: req.body.email}, (err,user) => {
    // db에 user에 대한 정보가 없다면 res.json에 로그인실패 메시지를 반환
    if (!user) {
      return res.json({
        loginSuccess: false,
        message:"이메일오류"
      })
    }
    // 유저가 존재한다면 비밀번호는 맞는가?
    user.comparePassword(req.body.password ,(err, isMatch) => {
      // ismathch 비밀번호 비교 내장함수
      if (!isMatch)
      // 틀리면 틀림메세지 반환
        return res.json({ loginSuccess: false, message: "비밀번호틀림"})
  
        // 비밀번호와 아이디 모두 옳다면
        user.generateToken((err,user) =>{
          // err 발생시 에러반환
          if (err) return res.status(400).send(err)
          // err 발생 안할 시, 저장소(cookie)에 x_auth란 이름을 만듬, 그 후 성공메시지 전달
          res.cookie("x_auth", user.token)
          .status(200)
          .json({loginSuccess: true, userId: user._id})
        })
      })
  })
})

app.get('/api/users/auth',auth,(req,res) => {
  res.status(200).json({
    _id: req.user._id,
    // isAdmin: req.user.role === 0 ? false : true
    email : req.user.email,
    isAuth: true,
    name: req.user.name
  })
})

app.get('/api/users/logout',auth,(req,res)=>{
  User.findOneAndUpdate({ _id:req.user._id},
    {toekn:""}
    , (err, user) => {
      if (err) return res.json({ success: false,err})
      return res.status(200).send({
        success: true
      })
    }
    )
})
// app이 리슨되면 아래 함수가 실행됌
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

