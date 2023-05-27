# ePUBReader

### ePUB 구조 분석도

```
// (0). 필수 고정파일들 
- META-INF
|	- container.xml
|	- (encrytion.xml)
|   - (com.apple.ibooks.display-option.xml)
- mimetype

// (1). 필수 파일들
- content.opf
- toc.ncx
- (page_map.xml)

// (2). 유동적인 파일들
- OEBPS
|	- Fonts
|	|	- ttf파일(생략)
|	- Images
|	|	- image들(생략)
|	- Styles
|	|	- style.css들(생략)
|	- Text
|	|	- xhtml들(생략)
- iTunesMetadata.plist
```

(1). upload 시 mimetype과 확장자(.epub)를 확인하고 epub파일이 아니라면 return

(2). META-INF > container.xml을 찾아서 content.opf 파일 위치를 확인

- 암호화된 파일은 일단 고려하지 않는다

(3). content.opf 파일을 기준으로 파일들의 위치를 기록( => 이 과정이 어떻게 진행될지 모름) 

※ 여기서 표준화를 시켜버리면 어떨까? => 이럴거면 epub 리더기를 만드는게 날까?

- apple 관련 파일들은 모두 무시한다(iTunes, com.apple)
- encrytion 파일도 나중에 고려한다.
- xpgt 확장자도 나중에 고려하며 이 파일이 있을시 error를 리턴하자.

(4). `spine`을 기준으로 toc.ncx와 page_map.xml 파일을 찾고 목차 기능 구현

(5). 목차를 기준으로 첫 페이지를 찾아서 렌더링을 하고 상단 메뉴바 또는 토글바를 이용하여 epub을 관리하자



### 변수들

(1). upload가 가능할까? 가능하다면 그 이후에 파일 내부 접근은 어떻게 하지?

(2). opf에서 서치는? 그게 zip 파일 내부에서 가능한 일이야?

(3). toc를 이용한 목차는 배열로? 어떻게 만들고 반응시킬거야?

(4). css는 어떻게..? pagenation으로 밀고나가야 에러가 없을 거 같은데

(5). 해상도 문제는 해결가능할까?

(6). 파서를 했다는 구조가 이해가 안가는데

(7). font나 확장자가 다른게 자동으로 될까?

(8). 혼합... 

---

### 추후 고려

(1). 암호화 관련

(2). 애플 ibook  관련

(3).  xpgt 관련

(4). epub ver2, 3 혹시 표준이 있는가?

---

### 수정

(1). 수정을 태그단위로 진행해..?

(2). 표준화하면 css를 갈아엎자는 건가요?

(3). 노션처럼 박스단위로 css를 만들어야할 거 같은데..

(4). 마찬가지로 사이즈 조절기능 구현 ==> 보조가 가능한건가?



