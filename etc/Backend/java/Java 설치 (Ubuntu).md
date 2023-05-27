# Java 설치(Ubuntu)

### java 설치

따로 어렵게 설치할 필요없이 ubuntu 설치를 지원하기 때문에 

1. 터미널에서 java 설치
2. 환경변수 설정 

두 가지만 하면 쉽게 설치가 된다



### 1. 터미널에서 설치

```
$ sudo apt-get update 
$ sudo apt-get install openjdk-8-jdk
```

- 이후, java -version을 이용하여 제대로 설치되었는지 확인하자



### 2. 환경변수 설정

```
$ readlink -f $(which java)
```

- 이 경로를 통해서 자바의 경로를 찾아보자.
  - ex). /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
  - 위 예제에서 /bin/java를 제외한 /usr/lib/jvm/java-8-openjdk-amd64/jre가 경로이다.



- 그 후 최상위 폴더에서 `/etc/profile` 문서에 가장 하단에 아래 코드를 넣고 저장하자 

```
export JAVA_HOME=[경로]
export PATH=$PATH:$JAVA_HOME/bin

ex). 
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
export PATH=$PATH:$JAVA_HOME/bin
```

​	- `sudo vi` 를 이용하여 수정하고는 하는데 저는 ux가 불편해서 text 편집기로 수정하였습니다.

 

- 환경변수 적용하기

```
$ source /etc/profile
```

​	 - 위 코드를 치고 재부팅을 하면 환경변수 적용 완료



- 적용 확인하기

```
echo $JAVA_HOME
```

이를 쳤을 때 제대로 `/usr/lib/jvm/java-8-openjdk-amd64` 가 나오면 성공입니다



### 참고자료

개인블로그 : https://i5i5.tistory.com/266

stackoverflow: https://stackoverflow.com/questions/9612941/how-to-set-java-environment-path-in-ubuntu
