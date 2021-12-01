import axios from 'axios';
import './App.css';
import imga from './아이유.png'
function App() {
  var client_id = 'y0s6ug2zk7';
  var client_secret = 'tO5Nz8R6i3XqLgT134jEzS7b8HUJBQL5xCTRbEqc';
  var formData = {
      image: imga// original image file
    };
  var  headers = {
    'X-NCP-APIGW-API-KEY-ID':client_id, 
    'X-NCP-APIGW-API-KEY': client_secret, 
    'Content-Type': 'multipart/form-data'
    };
    
 
  const requestNaver = () => {
    axios.post("https://naveropenapi.apigw.ntruss.com/vision/v1/face/", formData,headers)
    .then (response => {
      console.log(1)
      console.log(response)
    }
      // console.log(response.headers['content-type'])
    );
      // console.log( request.head  );
      // _req.pipe(res); // 브라우저로 출력
  };

  /* Start Express Server */
  // app.listen(3000, function () {
  //   console.log('http://127.0.0.1:3000/face app listening on port 3000!');
  // });
  //     console.log(1)
      
  // }


  return (
    <div className="App">
      
        <div className="help-tip">
          <button onClick={requestNaver}>kkk</button>
          <p>알림메시지</p>
        </div>
        </div>
        
    
  );
}

export default App;
