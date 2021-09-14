# sqoop 설치하기



### scoop 설치 및 실행 확인 

```python
# 참고주소 https://hhgg.tistory.com/6https://hhgg.tistory.com/6

# 최근 안정 버전 (1.4.7) 다운로드
wget http://mirror.navercorp.com/apache/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz

# 압축 해제
tar xvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz

# 실행 확인
cd sqoop-1.4.7.bin__hadoop-2.6.0
bin/sqoop help

# 텍스트 편집기로 .bashrc 파일 열기 & 스쿱의 환경변수 추가 
vi ~/.bashrc  
  
# scoop config 
export SQOOP_HOME= "/user/local/hadoop/sqoop-1.4.6.bin__hadoop-2.0.4-alpha"
export PATH=$PATH:$SQOOP_HOME/bin
    
# 참고주소2 https://mygameprogamming.tistory.com/36
# scoop config2
[hadoop@master ~]$ cd /usr/local/sqoop/conf
[hadoop@master conf]$ mv sqoop-env-template.sh sqoop-env.sh
[hadoop@master conf]$ vi sqoop-env.sh

[sqoop-env.sh]
export HADOOP_COMMON_HOME=/usr/local/hadoop
export HADOOP_MAPRED_HOME=/usr/local/hadoop

```

- 경로를 상대적으로 잘 파악해서 할 것



### jdcd 설치

```python
[hadoop@master ~]$ cd /usr/local/sqoop
[hadoop@master sqoop]$ wget http://ftp.ntu.edu.tw/MySQL/Downloads/Connector-J/mysql-connector-java-5.1.47.tar.gz
# https://downloads.mysql.com/archives/c-j/로 접속하여 firefox로 다운 받을 것
[hadoop@master sqoop]$ tar -xzvf mysql-connector-java-5.1.47.tar.gz
[hadoop@master sqoop]$ cd mysql-connector-java-5.1.47
[hadoop@master mysql-connector-java-5.1.47]$ cp mysql-connector-java-5.1.47.jar /usr/local/sqoop/lib
```

```python
# 필요한지 정확히 모름
http://commons.apache.org/proper/commons-lang/download_lang.cgi
 $SQOOP_HOME/lib에 위치
```



### mysql 설치 

- mysql 설치를 꼭 해야하는지 정확히 모른다.
- 현재 나의 경우 local을 사용해서 설치를 했다.
- https://dejavuqa.tistory.com/317 



### mysql root 비밀번호 설정

- https://www.lesstif.com/dbms/mysql-error-1698-28000-89555999.html

- 이 설정을 해야 root로 접속이 가능하다
- 이 파일이 mysql을 가리켜야한다.



### mysql 데이터 넣기

참조: https://blog.naver.com/PostView.naver?blogId=shyoo_1990&logNo=221275082481&parentCategoryNo=&categoryNo=33&viewDate=&isShowPopularPosts=true&from=search

접근 권한 미설정



### wordcount 오류 해결법

```
https://m.blog.naver.com/firstpcb/221884571315
```



### import

```
bin/sqoop import --connect jdbc:mysql://127.0.0.1:3306/testdb?useSSL=false -username root -password qwert1234 --m 1 --table WordTable

```





### export

```
bin/sqoop export --connect jdbc:mysql://127.0.0.1:3306/exdb?useSSL=false -username root -password qwert1234 --m 1 --table exWordTable --export-dir WordTable --input-fields-terminated-by , 

bin/sqoop export --connect jdbc:mysql://127.0.0.1:3306/exdb?useSSL=false -username root -password qwert1234 --m 1 --table exword --export-dir WordTable --input-fields-terminated-by , --bindir /home/hadoop/sqoop^C




```

