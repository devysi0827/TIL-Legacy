# Input click 불가 오류 

### 문제

- movit project에서 새로고침 전에는 input을 클릭할 수 없는 오류가 발생하였다.

  

### 원인

- 해당 문제의 원인은 drag component를 만든 것이였다! drag component가 마우스를 잡고 있어서 최초로딩시에는 input을 클릭할 수 없었던 것이다.



### 해결책

- 해당 컴포넌트를 삭제했다.
- 강제로 새로고침을 한 번 시켰다.