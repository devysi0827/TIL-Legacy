const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
// 10글자 짜리 salt를 생성
const saltRounds = 10;
const jwt = require('jsonwebtoken');

const userSchema = mongoose.Schema({
    name: {
        type: String,
        maxlength: 50
    },
    email: {
        type:String,
        trim: true,
        unique:1
        // sparse:true
    },
    password: {
        type:String,
        minlength: 1
    },
    lastname: {
        type: String,
        maxlength: 50
    },
    image: String,
    token: {
        type: String
    },
    tokenExp : {
        type:Number
    }

})


// user 정보를 저장하기 전 실행하는 함수
// 이 경우 bcrypt를 이용해 비밀번호를 암호화할 예정
userSchema.pre('save', function(next){
    // 위에 userschema를 가리킴
    var user = this;

    // bcrypt_salt생성
    if(user.isModified('password')) {
        bcrypt.genSalt(saltRounds, function(err, salt) {

            if(err) return next(err)

            bcrypt.hash(user.password, salt, function(err, hash) {
                // Store hash in your password DB.
                if(err) return next(err)
                // 유저의 패스워드를 해쉬로 치환
                user.password = hash
                next()
            });
        });
    } else {
        next()
    }
})

userSchema.methods.comparePassword = function(plainPassword, cb) {
    bcrypt.compare(plainPassword, this.password, function(err, isMatch){
        if (err) return cb(err)
        cb(null, isMatch)
    })


}

userSchema.methods.generateToken = function(cb) {
    var user = this
    var token = jwt.sign(user._id.toHexString(), 'secretTOKEN')
    user.token = token
    user.save(function(err,user) {
        if (err) return cb(err)
        cb(null, user)
    })
}

userSchema.statics.findByToken = function(token,cb) {
    var user = this;
    jwt.verify(token, 'secretTOKEN' ,function(err,decoded){
        user.findOne({ "_id": decoded, "token": token}, function(err,user){
            if(err) return cb(err)
            cb(null,user)
        })
    })
}

const User = mongoose.model('User',userSchema)
module.exports = {User}

