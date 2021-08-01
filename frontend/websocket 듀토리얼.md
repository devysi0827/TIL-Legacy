# websocket 듀토리얼

## 1. blog1 : https://november11tech.tistory.com/173

1. sockjsclient 컴포넌트 생성 (url = websocket config endpoint)
2. topics 설정 => 구독링크들 의미
3. sendTo, sendTemplate로 해당 backend 함수로 메시지 전송

![image-20210728022840439](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210728022840439.png)





## 2.blog2 : https://velog.io/@ehdrms2034/Spring-boot-React%EB%A1%9C-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%B1%84%ED%8C%85%EB%B0%A9-%EC%A0%9C%EC%9E%91%ED%95%98%EA%B8%B0

SockJS : WebSocket과 유사한 객체를 생성해주는 라이브러리,
웹소켓을 형성하거나 웹소켓을 지원하지 않을 경우에는, Long 폴링 방식(확실하지 않음)을 통해서 소켓 통신을 구현.

Stomp : Simple (or Streaming) Text Orientated Messaging Protocol의 약자로써, 메시지로 소켓 통신을 구현하는 경우 좀 더 효율적으로 구성을 할 수 있게 해준다.



```react
import * as React from "react";
import { ChatPresenter } from "../Presenter/ChatPresenter";
import "./ChatContainer.scss";
import { message } from "antd";
import {useEffect} from "react";
import SockJS from 'sockjs-client';
import Stomp from 'stompjs';

export type message = {
  username: string;
  content: string;
};

let sockJS = new SockJS("http://localhost:8080/webSocket");
let stompClient : Stomp.Client = Stomp.over(sockJS);
stompClient.debug= () => {};

export const ChatContainer = ({}) => {
  const [contents, setContents] = React.useState<message[]>([]);
  const [username, setUsername] = React.useState('');
  const [message, setMessage] = React.useState("");

  useEffect(()=>{
    stompClient.connect({},()=>{
      stompClient.subscribe('/topic/roomId',(data)=>{
        const newMessage : message = JSON.parse(data.body) as message;
        addMessage(newMessage);
      });
  });
  },[contents]);
  
  const handleEnter = (username: string, content: string) => {
    const newMessage: message = { username, content };
    stompClient.send("/hello",{},JSON.stringify(newMessage));
    setMessage("");
  };

  const addMessage = (message : message) =>{
    setContents(prev=>[...prev, message]);
  };

  return (
    <div className={"container"}>
      <ChatPresenter
        contents={contents}
        handleEnter={handleEnter}
        message={message}
        setMessage={setMessage}
        username={username}
        setUsername={setUsername}
      />
    </div>
  );
};
```



```
// paht  : CHATTING/chat/App.js

import React, {useState, useEffect} from 'react';
import io from 'socket.io-client';
import TextField from '@material-ui/core/TextField';
import './App.css';

const socket =  io.connect('http://localhost:4000')

function App() {
  const [state, setState] = useState({message:'', name:''})
  const [chat,setChat] =useState([])

  useEffect(()=>{
    socket.on('message',({name,message})=>{
      setChat([...chat,{name,message}])
    })
  })

  const onTextChange = e =>{
    setState({...state,[e.target.name]: e.target.value})
  }

  const onMessageSubmit =(e)=>{
    e.preventDefault()
    const {name, message} =state
    socket.emit('message',{name, message})
    setState({message : '',name})
  }


  const renderChat =()=>{
    return chat.map(({name, message},index)=>(
      <div key={index}>
        <h3>{name}:<span>{message}</span></h3>
      </div>
    ))
  }

  return (
    <div className='card'>
      <form onSubmit={onMessageSubmit}>
        <h1>Message</h1>
        <div className="name-field">
          <TextField 
          name ="name" 
          onChange={e=> onTextChange(e)} 
          value={state.name}
          label="Name"/>
        </div>
        <div >
          <TextField 
          name ="message" 
          onChange={e=> onTextChange(e)} 
          value={state.message}
          id="outlined-multiline-static"
          variant="outlined"
          label="Message"/>
        </div>
        <button>Send Message</button>
      </form>
      <div className="render-chat">
        <h1>Chat log</h1>
        {renderChat()}
      </div>
    </div>
  );
}

export default App;
```

