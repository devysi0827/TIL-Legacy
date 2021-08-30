# react: event

### 개념

html에서 일어나는 event를 다루는 법



### 코드

```react
import React, { Component } from 'react'

export default class PhoneForm extends Component {
    
    state = {
        name: '',
        phone: '',
    }

    handlechange = (e) => { 
        this.setState({
            [e.target.name]: e.target.value
        })
    }
    
    render() {
        return (
            <form>
                <input
                    name ="name"
                    placeholder="이름" 
                    onChange={this.handlechange} 
                    value={this.state.name}
                    />
                <input 
                    name="phone" 
                    placeholder="전화번호" 
                    onChange={this.handlechange} 
                    value={this.state.phone}
                    />
                
                {this.state.name}
                {this.state.phone}
            </form>
        )
    }
}

```



1. handlechange 

   상태변경함수 앞에 보통 handle을 붙인다.  `onChange`를이용하여 `input`과 연결하여 사용한다

   

2. (e)

   event의 약자 해당 event를 불러온다.

   

3. event.target 

   event를 일으킨 대상, 이 예제의 경우 각 input이 대상이 된다

   

4. 코드 해설

   해당이벤트가 발생시, input에서 handlechange를 실행시킨다.

   this.setState로 상태를 변경

   변경 대상은 e.target.name === 해당 이벤트가 발생한 input의 `name` 속성

   변경 내용은 e.target.value === 해당 이벤트가 발생한 input의 `value` 속성

   
