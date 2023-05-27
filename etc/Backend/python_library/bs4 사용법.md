# bs4 사용법

### 서두

- 공식문서 : https://beautiful-soup-4.readthedocs.io/en/latest/

- 목적: `python`에서 '문서'(`html`, `xml` 등)를 `parsing` 하기 위해서
- 설치

```python
pip install beautifulsoup4
# lxml 설치하면 xml parser를 사용할 수 있거나 속도가 빨라지는 등 장점이 있지만 추가 설치를 해야하며 굳이 할 필요는 없다.
pip install lxml
```

- import

```python
from bs4 import BeautifulSoup
```

- 적용하기

1.  html file일 경우,

```
with open("index.html") as fp:
    soup = BeautifulSoup(fp)
```

2. html string일 경우,

```python
soup = BeautifulSoup(zipdata, "lxml") # html.parser나 제공하는 것으로 lxml 대체가능
```

