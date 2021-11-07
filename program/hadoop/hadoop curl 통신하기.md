# curl을 통한 url 통신

### curl이란?

curl은 오픈 소스로 개발되어 윈도우와 리눅스에 기본 설치되고 있는 웹 개발 툴로써 **http, https, ftp, sftps, smtp, telnet 등의 다양한 프로토콜과 Proxy, Header, Cookie 등의 세부 옵션까지 쉽게 설정**할 수 있습니다.

출처: https://kibua20.tistory.com/148 [모바일 SW 개발자가 운영하는 블로그]



### 주소 및 curl 통신 설정

1. hdfs-site.xml 파일을 찾아준다

2. 아래와 같은 내용을 추가한다

   ```xml
   	<property>
         <name>dfs.webhdfs.enabled</name>
         <value>true</value>
       </property>
     
     <property>
       <name>dfs.namenode.http-address</name>
       <value>0.0.0.0:50070</value>
     </property>
   ```

   - dfs.webhdfs.enabled : 통신을 가능하게 true 설정
   - dfs.name.http-address: ubuntu 내부 hdfs 주소를 설정 기본값은 localhost:9870인듯 하다

출처: https://socurites.tistory.com/168 [Socurites The Wisdom]



### curl 명령어 정리

- hdfs 리스트 가져오기 /user/hadoop 부분을 수정하면 더 내부를 볼 수 있다


  curl -XGET "http://0.0.0.0:50070/webhdfs/v1/user/hadoop?op=LISTSTATUS" -i

- hdfs 파일 읽기

  curl -i -L "http://0.0.0.0:50070/webhdfs/v1/user/hadoop/WordTable/part-m-00000?op=OPEN"



- 참고문서: http://hadoop.apache.org/docs/r1.0.4/webhdfs.html#FsURIvsHTTP_URL
