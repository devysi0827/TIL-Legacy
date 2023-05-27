# ePUB 분석

### ePUB이란?

- **EPUB**(electronic publication)

- 개방형 자유 전자서적 표준
- Open Publication Structure 2.0, 이는 내용의 형태를 정의한다.
- Open Packaging Format (OPF) 2.0, 이는 XML로 구성된 .epub의 파일 구조를 정의한다.
- OEBPS Container Format(OCF) 1.0, 모든 파일들을 ZIP으로 압축 저장한다.



### 구조(ver2)

![ePUB 분석](/home/seil/Desktop/React 문서/react 이미지파일/ePUB 분석.png)




### META-INF

- 일반적으로 이 폴더내부에 Manifest file 또는 Metadata를 담지만 ePUB에서는 container.xml 파일을 이용하여 메타데이터의 위치를 지정해줌
- ibook 같은 경우 ibook 설정파일이 추가로 담긴다.
- 반드시 필요한 폴더이며, 루트 디렉토리이기 때문에 위치도 변경되어서는 안된다.



### minetype

- 반드시 폴더 최상단에 존재해야만 한다.
- ePUB파일임을 명시해준다.



### OPF파일(in OEBPS)

아래 것들을 제공하나 양식은 정해진 것이 없음

- 리소스 (media, css, font)
- 매니페스트 : 모든 파일을 나열하고 파일 형식을 지정합니다. 여기 등록되지 않은 파일은 정상적으로 불러와지지 않을 수 있습니다.
- 메타데이터 : 서명, 언어, 타이틀등의 정보 제공
- spine (목차) : 선형구조 책에서 idref로 파일을 식별 및 독자를 위한 순서제공
- guide(파일 위치)
- com.apple.ibooks.display-options.xml : Apple/ibook 전용 setting 파일



### NCX파일 (in OEBPS)

- 최적의 텀색을 위해 <pageList> 와 <navMap> 을 이용하여 EPUB 내 탐색을 돕습니다.

  - navMap : playlist를 만들어서 해당 페이지를 불러오는 방법
  - pageList: 모든 xhtml에 지정된 페이지를 부여하고 해당 페이지를 부르는 방법

  

###### cf) 1. ePUB 기준

- 다양한 기준이 존재하며 해당 기준이 어긋날 시, img, xhtml, svg 등 파일로딩에 문제가 생길 수 있음
- 이와 관련된 기준은 밑에 첨부된 공식문서들을 참고하길 바람.



###### cf) 2. Tips for Improving Performance in Books with JavaScript Interactivity(ibook)

성능을 향상시키려면 다음 사항에 유의하십시오.
● 이미지 최적화는 성능 향상의 핵심입니다. "고정 레이아웃에서 이미지 최적화하기"를 참조하십시오.
이미지 최적화 방법은 책”(50페이지)을 참조하십시오.
● 페이지당 애니메이션 수를 제한합니다. 가장 필요한 것만 보관하십시오.
● 애니메이션에 CSS(JavaScript 아님)를 사용합니다.
● 위/아래/왼쪽/오른쪽 위치를 설정하는 대신 CSS 3D 변환을 사용합니다. 이것은 더 부드러운 전환을 만듭니다
하드웨어 가속이지만 우선 순위가 높은 요소를 위해 예약해야 하기 때문입니다.
● 페이지 복잡성을 줄입니다.
● JavaScript가 책에 맞게 조정될 때 성능이 가장 좋습니다. 타사 JavaScript 라이브러리는 종종
크며 성능이 저하될 수 있습니다.(ibook library를 의미)




### 참고문서

ibook 및 epub 설명(그림참조) : https://itunespartner.apple.com/assets/downloads/ibookstore-asset-guide-5-0.pdf

epub w3c 공식설명 : https://www.w3.org/publishing/epub3/epub-spec.html