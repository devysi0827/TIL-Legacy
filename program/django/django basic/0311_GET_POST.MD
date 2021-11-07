0311



1. csrf -사이트(html) 위조

   - csrf를 막기위해서는 `우리 서버로부터 발행하였다는 확신`이 필요함.
- 이걸 csrf_token을 이용하여 위조여부를 확인.
     - MASTERAPP_ setting.py_ MIDDLEWARE_ 'django.middleware.csrf.CsrfViewMiddleware'에서 이를 체크하고 위조일 시 거부당한다.
   - csrf_token은 1회성으로 매번 갱신되며, 이는 브라우저, F12에서 input=hidden으로 확인할 수 있다.
- token 검사는 POST형식에서만 진행한다.( 아마!)



2. GET, POST
   - GET은 정보입력, POST는 정보읽기를 목적으로 주로 사용한다.
   - 다만, 어제 실습과 같이, 둘 다 사용이 가능하다
     - (어제실습에서 GET을 이용하여 정보를 읽었다.)
   - 주소창의 입력, 등 form을 통한 전달(제출과 같은 버튼 클릭)을 `제외한` 모든 방식은 GET방식이다.
   - 반대로, 현재 배운 범위에서는 `form을 통한 제출(버튼 클릭을 통한 이동)만` POST방식이다.



3. GET, POST 심화

   - POST 전달을 하였지만 request.GET.get 을 사용시 GET정보가 없으므로 None을 반환한다.

   - POST와 GET의 차이

     - GET은 정보보안이 없기때문에 브라우저 주소창으로 접근이 가능함

       EX) www.naver.com/ssafy/17 등등 정보를 입력하면 바로이동

       편리성 UP, 보안성 DOWN

     - POST는 보안과정이 있기때문에 주소창에 바로치면 TOKEN이 없는 GET전달을 거부함.

       따라서, 위와 같은 주소창 접근은 불가능하고 오직 클릭으로 순서에 맞게 이동해야함

       편리성 DOWN 보안성 UP

   - POST, GET은 정보전달방식의 차이

     - 정보는 반드시 이분법적으로 POST나 GET으로만 오기 때문에 if-else 구문을 이용하여 지정해 줄 수 있다.
     - ex). 같은 index.url 호출에 대해서, POST => (정보)입력페이지 GET => 완성된 문서 페이지  로 각각 보내 줄 수 있다.

