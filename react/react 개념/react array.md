# react: array

https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map



## 배열 추가하기

배열에 특정 값을 추가한다.

단, 이 때 데이터의 불변성을 반드시 지켜야한다!!!



### concat

```react
handleCreate = (data) => {
    this.setState({
      information: this.state.information.concat(data)
    })
  }
```

- concat 내장함수를 이용하면, 기존의 데이터를 변경하지 않고 배열에 데이터를 추가할 수 있다.



### 데이터인자를 확장하기

```react
 handleCreate = (data) => {
    this.setState({
      information: this.state.information.concat({
        ...data,
        id: this.id++
      })
    })
  }
```

- `...data , id: 이하생략` 

  ...data로 확장시킨 뒤 원소를 추가

```react
information: this.state.information.concat({
        Object.assign({},data,{
    		id: this.id++
			})
      })
```

- {}에 data와 {id...}을 넣어서 합친다 (1항에 2항과 3항을 합쳐서 넣는다)

----------------------------------

## 배열 렌더링하기

```react
const list =data.map(
            info=> <PhoneInfo info={info} key={info.id} />)
        return (
            <div>
                {list}
            </div>
        )
```

- map함수: .map( n => n*n)

  내부 n을 n*n으로 만들어서 반환함

  여기서는,  `data` 내부 `info` 값을 `PhoneInfo`내부 info에 `info`값을 넣어주고 해당` id`를 key로 해준다



--------------------------------

## 배열 제거,수정하기

불변성의 유지가 매우 중요

`.slice` or `.filter` 를 사용

`.slice().concat(....)`으로 slice한것끼리 이을 수 있음

또는

... 확장연산자를 사용

`. filter`를 이용하여, 조건문 형식으로 필터링가능

두 함수 모두, 원래 배열을 건드리지 않고 수정된 값을 가져옴



-----------------

### 배열 관리하기

