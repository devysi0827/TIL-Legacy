# ePUB 구조 분석

### ePUB 구조 분석 요약

아래 상세구조들을 종합하여 작성한 구조 분석으로 아래 구조들은 따로 다시 볼 필요가 없음

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

- META-INF(container.xml)와 mimetype을 제외한 그 어떠한 것도 위치와 이름이 정확하지 않음. 오직 META-INF(container.xml)와 mimetype만 믿을 것.



- (0) 이하 파일들은 위치와 이름이 고정이며 필수적임
  - META-INF : root directory를 담당하며 항상 최상위폴더에 위치함
  - contatiner.xml : opf 파일의 상대적인 위치를 표시. opf 파일은 모든 메타데이터를 표시함
  - encrytion.xml : 저작권과 암호화 작업을 담당. 필수적이지는 않음
  - com.apple....xml : apple 기기에서 사용자 설정을 담당. 필수아님
  - mimetype : epub파일임을 명시함




- (1) 이하 파일들은 필수적인 파일들이나 위치와 이름이 제각각으로 통일성이 없음

  - .opf : 단 하나의 파일이 존재하며, container.xml이 위치를 표시, 모든 파일의 위치를 알려준다
  - .ncx : 단 하나의 파일이 존재하면 .opf가 위치를 표시, 목차역활을 해준다.
  - .page_map.xml :  필수는 아니지만 .ncx의 목차역활을 보조해줄 수 있다.




- (2) 이하 파일들은 필수가 아니지만 구조상 항상 존재하며 매우 많은 변수를 창출한다.

  - Fonts : odf 와 ttf 방식 글꼴 두개가 주로 존재한다. 책인 만큼 보통 여러개의 글꼴이 있따
  - Images : jpeg, png, gif, svg 등 거의 대부분의 이미지가 가능하다. 역시 보통 여러개의 삽화가 들어간다.
  - Styles : css 파일로 하나가 주를 이루지만, 페이지마다 css를 넣기도 하고 표지와 목차 전용 css만 만들기도 하는등 개수가 매 번 다르다.
    - xpgt라고 xml의 확장판을 사용하는 epub 파일도 존재한다
    - 내부 css는 정말 자유로우며 아무런 제약이 없다.
  - Text : 주제에 메인이 되는 글이며,  html이기 때문에 css와 image 삽입도 여기서 일어난다.
    - xhtml, html 크게 두 가지로 나누어진다
    - 저 두 양식을 보통 따로 쓰는데 낮은 확률로 혼합해서 쓴다.
    - 보통 하나의 폴더에 넣어두는데, 표지는 다른 폴더에 위치시키는 사람이 적지 않다.
  - iTunesMetadata.plist : iTunes에서 사용한 적 있다면 등록되는 Metadata파일이다.



-----




### ePUB의 구조1

```
- META-INF
|	- container.xml
- OEBPS
|	- Images
|	|	- image들(생략)
|	- Styles
|	|	- style.css
|	- Text
|	|	- xhtml들(생략)
|	- content.opf
|   - toc.ncx
- mimetype
```

- 이 폴더구조를 기준으로 삼아서 이하  추가적인 내용들을 서술
- 중복되는 변경점은 따로 추가 서술하지 않음



### ePub의 구조2

```
- META-INF
|	- container.xml
|	- com.apple.ibooks.display-option.xml
- OEBPS
|	- Fonts
|	|	- odf 글꼴들(생략)
|	- Images
|	|	- image들(생략)
|	- Styles
|	|	- stylesheet.css
|	- Text
|	|	- html들(생략)
|	- content.opf
|   - toc.ncx
- mimetype
```

- 폰트 폴더 추가
- xhtml -> html
- css파일 이름 변경
- apple option 파일 추가 



### ePub의 구조3

```
- META-INF
|	- container.xml
- OEBPS
|	- stylesheet.css
|	- content.opf
|   - toc.ncx
|	- xhtml들(생략)
- mimetype
- iTunesMetadata.plist
```

- iTunesMetadata.plist는 ios임시배포파일
- OEBPS에 Text폴더 없이 배치



### ePub의 구조4

```
- META-INF
|	- container.xml
- OEBPS
|	- Fonts
|	|	- ttf파일(생략)
|	- Images
|	|	- image들(생략)
|	- style.css
|	- xhtml들 (생략)
- 9781250170071_epub_opf_r1.opf === content.opf
- 9781250170071_epub_ncx_r1.ncx === toc.ncx
- mimetype
- nav.xhtml
```

- container.xml에서 정확히 명시하면 `content` 라는 이름이 아니여도 사용가능
- 표지 파일(xhtml)을 최상단으로 꺼내는 사람도 있음



### ePub의 구조5

```
- META-INF
|	- container.xml
- Images
|	- image들(생략)
- Text
|	- html들(생략)
- page_styles.css
- stylesheet.css
- content.opf
- toc.ncx
- mimetype
- cover.jpeg
- titlepage.xhtml
```

- font를 다운로드 대신 page_styles.css로 사용
- 표지만 xhtml로 xhtml, html의 혼합사용
- 표지커버를 최상단으로 배치



### ePub의 구조6

```
- META-INF
|	- container.xml
- OPS
|	- Images
|	|	- image들(생략)
|	- Styles
|	|	- css들생략)
|	- xhtml
|	|	- xtml들(생략)
|	- content.opf
|   - toc.ncx
- mimetype
```

- css 파일을 여러개를 사용할 수 있다. (ebook을 링크기능등으로 페이지 관리해서 그런듯)



### ePub의 구조7

```
- META-INF
|	- container.xml
- OPS
|	- Images
|	|	- image들(생략)
|	- Styles
|	|	- style.css
|	- xhtml
|	|	- xtml들(생략)
|	- content.opf
|   - toc.ncx
|	- _page_map_.xml
- mimetype
```

- page_map.xml을 이용해서 spine을 보충해주는 듯 한데 굳이 필요해보이지 않는다. 실제 적용 후 확인해볼 것



### ePub의 구조8

```
- META-INF
|	- container.xml
|   - encryption.xml
- OPS
|	- Images
|	|	- image들(생략)
|	- Styles
|	|	- style.css
|	|	- page-template.xpgt
|	- xhtml
|	|	- xtml들(생략)
|	- content.opf
|   - toc.ncx
|	- _page_map_.xml
- mimetype
```

- encryption.xml 로 암호화 파일이 추가되었다/
- page-template.xpgt로 XML 스타일시트로 확장을 담당한다. 이 파일이 없을 시 배치가 달라지는 걸 확인





### 참고문서

- 서양음악사
- 교과서 속 전래동화 쏙쏙 뽑아 읽기 1학년
- 경혈지압과 척추교정요법전서
- How to Draw a Character The Foolproof Method by Soizic Mouton
- How To Draw Sketch and draw anything, anywhere with this inspiring and practical handbook by Jake Spicer
- Music Theory 101 From Keys and Scales to Rhythm and Melody, an Essential Primer on the Basics of Music Theory
- SOMETHING I WANT TO TELL YOU   essay 