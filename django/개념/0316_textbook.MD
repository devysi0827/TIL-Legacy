#### Date: 0316

#  Django Form



## django Form

- 유효성 검사 도구 및 중요방어수단
- 렌더링을 위한 데이터 준비 및 재구성
- 데이터에 대한 HTML forms 생성
- 클라이언트로부터 받은 데이터 수신 및 처리



# Form Class

- django Form의 핵심
- field, field배치, 디스플레이 widget, 초기값, 에러메시지등 결정
- 데이터 유효성, 재출력, 유효한 데이터에 대한 요구동작 수행 등 해야할 작업과 반복 코드를 줄여줌



# ModelForm Class

- model을 통해 Form Class를 만들 수 있는 helper

- Meta Class

  - Model의 정보를 작성하는 곳
  - 해당 model에 정의한 field 정보를 Form에 적용하기 위해 사용

  

# Form & ModelForm

- Form 
  - 어떤 모델에 저장해야하는지 유효성 검사 이후 cleaned_data 딕셔너리를 생성
  - model에 연관되지 않은 데이터를 받을때 사용



- ModelForm 

  - django 가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
  - 어떤 레코드를 만들어야 할 지 알고 있으므로 바로 .save() 호출 가능

  

#  widgets

- django html input element 표현
- html 렌더링 처리
- 주의 사항
  - form fields와 혼동되어서는 안됨
  - input 유효성 검사를 처리
  - widgets은 웹페이지에서 input element의 단순 raw한 렌더링 처리



#  html 인풋 요소 표헌방법

- Form fields
  - input에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용됨

- Widgets
  - 웹 페이지의 HTML input 요소 렌더링 및 제출 된 원시데이터 추출을 처리
  - 하지만 widgets는 반드시 form fiedls에  할당됨



#  static files

- 요청한 그대로 수정없이 보여주면 되는 파일

  - 기본 경로: app_name/static/

  - ```html
    {% load static %}
    <img src ="{% static 'abc.png' %}" alt = "sample">
    ```



# static files in settings.py

- STATIC_ROOT
  - collectstatic이 배포를 위해 정적 파일을 수집하는 절대 경로
- STATIC_URL
  - STATIC_ROOT에 있는 정적파일을 참조할 때 사용하는 URL
- STATICFILES)DIRS
  - app내의 static 디텍토리 경로를 사용하는 것 외에 추가적인 정적 파일 경로 정의



# media

- 사용자가 웹에서 업로드 하는 정적파일 : image, pdf, video



# media files in setting.py

- media_root

  - 사용자가 업로드 한 파일을 보관할 디텍토리의 절대 경로
  - 실제 해당 파일의 업로드가 끝나면 어디에 파일이 저장하게 할 지 경로

- media_url

  - media_root에서 제공되는 미디어를 처리하는 url
  - 업로드 된 파일의 주소(url)을 만들어주는 역활
  - media_url은 static_url과 주소가 달라야 함

  - ```python
    urlpattens = [
        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

  - 