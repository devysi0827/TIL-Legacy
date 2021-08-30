# react: jsx 문법

1. 모든 태그는 닫혀있어야 한다.

   ```react
   <div></div>
   <input />
   ```

   

2. 모든 태그는 더 큰 태그에 둘러쌓여야한다.

   ```react
   <div>
   	<div>
   		hi
   	<div/>
   	<div>
   		bye
   	<div/>
   <div/>
   ```

   cf). Fragment를 import해오면, 불필요한 최상단 div 없이 사용 가능하다.



3. {}로 변수를 사용할 수 있다.

   ```react
   export default function App() {
     const name = "세일"
     return (
       <div className="App">
         <h1>message: {name}</h1>
       </div>
     );
   }
   ```

   cf). const: 상수, let: 변수로 지정하면 좋다



4. 삼항연산자를 이용하여, {} 내부에서 if문 처럼 사용이 가능하다

   ```
      { 
           1+1 ===3
             ? (<div>ok</div>)
             : (<div>no</div>) 
      }
      
      {
        name === "세일" && <div>세일일때만 표시됨</div>
      }
   ```

   

5. 함수에서는 내부에서 if문을 사용한다.(위에 경우들은 return 내부)

   ```react
   {
       (function() {
           if (value === 1) return <div>1</div>
           if (value === 2) return <div>1</div>
           if (value === 3) return <div>1</div>
           return <div>no</div>
       }) ()
   }
   ```

   - 함수를 {}로 감싸지 않으면 오류가 난다.
   - 함수를 바로 실행시키기 위해서 7번째줄에 함수 완료 후 ()을 써주어 바로실행시켰다.



6. css  style 적용하기

   ```
   export default function App() {
     
     const style = {
       backgroundColor : 'black',
       color:'white',
     }
     return (
       <div className="App" style={style}>
   
         안녕하세요
       </div>
     );
   }
   ```

   - style: 스타일 객체 형식으로 표현

   - 카멜케이스형식으로 사용하여야함 background-color => backgroundColor

     

7. className(class) 적용하기

   ```react
   import "./styles.css";
   
   export default function App() {
     return <div className="App">안녕하세요</div>;
   }
   ```

   - class 대신 className으로 사용하면 됌
   - class로 써도 되지만, className이 옳은 표현
   - css파일은 기존 css문법을 따름



8. 주석 작성법

   ````react
   {/* div 안에 있을 때는 이렇게!*/}
   <h1 //어떤 특정 태그안에 있을때는 이렇게도 가능 />
   ````

   

   

   