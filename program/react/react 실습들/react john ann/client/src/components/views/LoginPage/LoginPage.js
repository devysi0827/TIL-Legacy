
import { withRouter } from 'react-router-dom';
import React, {useState} from 'react'
import { useDispatch } from 'react-redux'
import {loginUser} from '../../../_actions/user_action'

function LoginPage(props) {
    const dispatch = useDispatch()

    const [Email, setEmail] = useState("")
    const [Password, setPassword] = useState("")

    const onEmailHandler = (event) => {
        setEmail(event.currentTarget.value)
    }

    const onPasswordHandler = (event) => {
        setPassword(event.currentTarget.value)
    }

    const onSubmitHandler = (event) => {
        event.preventDefault()
        let body = {
            email: Email,
            password : Password
        }

        dispatch(loginUser(body))
        .then(response=>{
            console.log(response)
            if (response.payload.loginSuccess) {
                props.history.push('/')
            } else {
                alert('Error')
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
                <label>password</label>
                <input type="password" value={Password} onChange={onPasswordHandler} ></input>
                <br />
                <button>
                    login
                </button>
                
            </form>
        </div>
    )
}

// export default LoginPage
export default withRouter(LoginPage)