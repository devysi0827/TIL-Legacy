import React, {useEffect} from 'react'
import axios from 'axios'
import {auth} from '../_actions/user_action'
import { useDispatch } from 'react-redux'


export default function (SpecificComponent, option, adminRoute = null) {
    function AuthenticationCheck(props) {
        const dispatch = useDispatch()
        useEffect(() => {
            dispatch(auth()).then(response=>{
                console.log(response)

                if(!response.payload.isAuth) {
                    if(option) {
                        props.history.push('/login')
                    }
                } 
                // else {
                //     if(option === false) {
                //         props.history.push('/')
                //     }
                    

                // }
            })
            axios.get('/api/users/auth')
        }, [])
        return (
            <SpecificComponent/>
        )
    }
    return AuthenticationCheck
}

