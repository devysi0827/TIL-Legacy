# local storage vs session storage vs cookie

### local storage

- 데이터가 따로 지우지 않으면  영구적으로 지속
- key-value 형태 저장
- 서버 부담 x
- ex) 자동로그인



### session storage

- 페이지를 닫으면 데이터 삭제
- key-value 형태 저장
- 서버 부담 x
- ex). 회원가입 입력정보, 장바구니



### cookie

- 서버와 통신을 위해 만들어져서 매 번 서버에게 요청을 보냄
- key-value 형태
- 만료일이 지나거나 삭제요청시 삭제
- ex) 다시보지않음 창



### 차이점 요약

local: 데이터가 따로 지우지 않는 이상 데이터가 계속 남는다

session: 페이지를 닫으면 데이터가 사라진다

cookie: 만료일자가 있다. 서버와 통신