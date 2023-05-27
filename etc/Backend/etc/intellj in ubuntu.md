# intellij in ubuntu

### 설치법

1. community version을 다운받아서 압축풀기
2. 해당 폴더에 압축풀기

```
 tar -zxvf ideaIC-2021.3.2.tar.gz 
```

3. 들어가서 실행이 되는지 확인하기

```
cd idea-IC-213.6777.52/bin
./idea.sh
```

- 이과정에서 정상적으로 실행된다면 intellij가 설치가 된 것이다.



### 경로바꾸기

- 매 번 해당 폴더에 들어가서 또는 해당경로를 쳐서 intellij를 키는 것이 귀찮다면 경로를 바꿔주는 방법이 있다.
- etc/bash.bashrc 파일에 아래 코드를 마지막 줄에 첨가한다
  - 이 때 아래 <> 경로는 실제 intellij가 설치된 경로이다.
  - bashrc 파일을 수정하는 것으로 만약 다른 os, 다른 shell을 사용할 경우 다른 파일을 수정해야할 수 도 있다.

```
alias intellij=<intellij 경로>bin/idea.sh
ex).
alias intellij=/home/seil/spring/idea-IC-213.6777.52/bin/idea.sh
```

 - 이후 아무 곳에서나 termial에 intellij라 치면 intellij가 실행된다



cf). alias 명령어는 '별명'이란 뜻으로 미리 정해둔 명령어를 단축어로 사용할 수 있게 해준다.



### 참고문서

개인블로그: https://king-minwook.tistory.com/69

개인블로그: https://dohk.tistory.com/191
