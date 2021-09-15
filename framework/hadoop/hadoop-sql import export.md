# Hadoop-MySql import export

## sqoop 설치하기

### sqoop이란?

- Sqoop은 Hadoop과 관계형 데이터베이스 또는 메인프레임 간에 데이터를 전송하도록 설계된 도구로입니다 ( HDFS(Haddop) <=> RDBMS(MySql, Oracle ...) ) 

- 공식문서 : https://sqoop.apache.org/docs/1.4.6/SqoopUserGuide.html#_introduction

  

### sqoop 설치 및 실행 확인 

```python
# 참고주소1 https://hhgg.tistory.com/6
# 1. 최근 안정 버전 (1.4.7) 다운로드
wget http://mirror.navercorp.com/apache/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
# 2. 알집 압축 해제, 
tar xvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
# 3. 실행 확인
cd sqoop-1.4.7.bin__hadoop-2.6.0
bin/sqoop help or sqoop help
# 4. 텍스트 편집기로 .bashrc 파일 열기 & 환경변수 추가 
vi ~/.bashrc  

export SQOOP_HOME=/home/hadoop/sqoop
export SQOOP_CONF_DIR=/home/hadoop/sqoop/conf
export PATH="$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH"

# 5-2. scoop 설정 변경
# 참고주소2 https://mygameprogamming.tistory.com/36
[hadoop@master ~]$ cd /usr/local/sqoop/conf
[hadoop@master conf]$ mv sqoop-env-template.sh sqoop-env.sh
[hadoop@master conf]$ vi sqoop-env.sh
[sqoop-env.sh]
export HADOOP_COMMON_HOME=/usr/local/hadoop
export HADOOP_MAPRED_HOME=/usr/local/hadoop

```

- 경로를 상대적으로 잘 파악해서 할 것( 위에 경로는 /home/hadoop을 기준으로 만듬)



### jdcd 설치

- jdbc란? sql을 접속하기 위해 java로 만들어진 connector프로그램이다. 

```python
[hadoop@master ~]$ cd /usr/local/sqoop
[hadoop@master sqoop]$ wget http://ftp.ntu.edu.tw/MySQL/Downloads/Connector-J/mysql-connector-java-5.1.47.tar.gz
# https://downloads.mysql.com/archives/c-j/로 접속하여 firefox로 다운 받을 것
[hadoop@master sqoop]$ tar -xzvf mysql-connector-java-5.1.47.tar.gz
[hadoop@master sqoop]$ cd mysql-connector-java-5.1.47
[hadoop@master mysql-connector-java-5.1.47]$ cp mysql-connector-java-5.1.47.jar /usr/local/sqoop/lib
```



```python
# 필요한지 정확히 모름, # 참고주소 https://hhgg.tistory.com/6
http://commons.apache.org/proper/commons-lang/download_lang.cgi
 $SQOOP_HOME/lib에 위치
```



## MySql 설치 및 데이터 관리

### mysql 설치 

- 서버접속을 위해 아마 필요한 듯 하다(부정확)
- 참조 : https://dejavuqa.tistory.com/317 



### mysql root 비밀번호 설정

- 이 설정을 해야 root로 접속이 가능하다
- mysql -u root -p 로 접속
- 참조 : https://www.lesstif.com/dbms/mysql-error-1698-28000-89555999.html



### mysql 데이터 넣기

- 접근 권한 미설정해도 된다.

- 참조 : https://blog.naver.com/PostView.naver?blogId=shyoo_1990&logNo=221275082481&parentCategoryNo=&categoryNo=33&viewDate=&isShowPopularPosts=true&from=search



## sqoop export import

공식문서를 참조하면 더 많은 명령어가 있고 더 많은 하위명령어가 존재한다.



### import 예시

```
bin/sqoop import --connect jdbc:mysql://127.0.0.1:3306/testdb?useSSL=false -username root -password qwert1234 --m 1 --table WordTable
```

- import: sqoop 명령어
  - --connect:  jdbc를 이용하여 연결할 주소:포트/사용db 를 표시한다
    - ?useSSL=false를 하면 보안관련 오류를 일단 무시할 수 있다
  - -username  <username> : 접속을 요청하는 db의 유저네임
  -  -password <password> : 접속을 요청하는 db의 패스워드
  - --m 1 : mapreduce 처리개수(파일 분할 개수)
  - --table <table name> : 저장할 hdfs 테이블네임(새롭게 생성되며 이미 있을 경우 에러)

### export 예시

```
bin/sqoop export --connect jdbc:mysql://127.0.0.1:3306/exdb?useSSL=false -username root -password qwert1234 --m 1 --table exWordTable --export-dir WordTable --input-fields-terminated-by "," 
```

- export: sqoop 명령어

  - --connect:  jdbc를 이용하여 연결할 주소:포트/사용db 를 표시한다

    - ?useSSL=false를 하면 보안관련 오류를 일단 무시할 수 있다

  - -username  <username> : 접속을 요청하는 db의 유저네임

  -  -password <password> : 접속을 요청하는 db의 패스워드

  - --m 1 : mapreduce 처리개수(파일 분할 개수)

  - --table <table name> : 반출할 hdfs 테이블네임

  - --export-dir <table name> :sql 테이블 네임

  - --input-fields-terminated-by  "," : " " 내부의 단위로 필드를 끊어서 읽음

     

### 기타 오류 해결법

1. 실행 dir을 /sqoop/lib로 하면 오류가 해결된다. (정확한 이유는 모르겠으나 경로 이상으로 추정)
   - https://m.blog.naver.com/firstpcb/221884571315
2. reverse를 붙이면 해결된다
   - 코드가 역순으로 import 또는 export 된다. export 될 경우, 넣을 때 db순서와 틀리면 자료형이 틀려서 에러가 발생한다.
