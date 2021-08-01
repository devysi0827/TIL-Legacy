
import { withRouter } from 'react-router-dom';
import React, {useState} from 'react'
import { useDispatch } from 'react-redux'
import {registerUser} from '../../../_actions/user_action'

function RegisterPage(props) {
    const dispatch = useDispatch()

    const [Email, setEmail] = useState("")
    const [Password, setPassword] = useState("")
    const [Name, setName] = useState("")
    const [ConfirmPassword, setConfirmPassword] = useState("")

    const onEmailHandler = (event) => {
        setEmail(event.currentTarget.value)
    }

    const onNameHandler = (event) => {
        setName(event.currentTarget.value)
    }

    const onPasswordHandler = (event) => {
        setPassword(event.currentTarget.value)
    }

    const onConfirmPasswordHandler = (event) => {
        setConfirmPassword(event.currentTarget.value)
    }

    const onSubmitHandler = (event) => {
        event.preventDefault()
        if (Password !==ConfirmPassword) {
            return alert('비밀번호틀림')
        }
        let body = {
            email: Email,
            password : Password,
            name: Name
        }

        dispatch(registerUser(body))
        .then(response=>{
            console.log(response)
            if (response.payload.success) {
                props.history.push('/login')
            } else {
                alert('Error signup')
            }
        })
    }


    return (
        <div style={{
            display: 'flex', justifyContent: 'center', alignItems: 'center', width: '100%', height: '100vh'
        }}>
            
            <form style={{display: 'flex', flexDirection: 'column'}}
            onSubmit={onSubmitHandler}>
                <label>Email</label>
                <input type="email" value={Email} onChange={onEmailHandler} ></input>
                <label>Name</label>
                <input type="text" value={Name} onChange={onNameHandler} ></input>
                <label>password</label>
                <input type="password" value={Password} onChange={onPasswordHandler} ></input>
                <label>confirm password</label>
                <input type="Confirmpassword" value={ConfirmPassword} onChange={onConfirmPasswordHandler} ></input>
                <br />
                <button>
                    회원가입
                </button>
                
            </form>
        </div>
    )
}

export default withRouter(RegisterPage)
