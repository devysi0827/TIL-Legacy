0322  


 # Auth Intro



#  settings. py

- 이전 세팅들은 모두 생략
  - urls, templates, git, 모두 미리 해놀 것



- 주석 없는 깨끗한 설명은 교수님 코드를 볼 것



- 기본 사용자 모델 설정하기

  ```python
  # 앱에서 만든 사용자 모델을 이 프로젝트의 기본 모델로 지정해주기 위해 가장 밑에 추가해준다.
  AUTH_USER_MODEL = 'accounts.User' 
  ```
  
- Q: 왜 사용하나요??
  - A: `from django.contrib.auth.models import User`로 불러도 되지만, 모델이 수정될 때, 너무 많은 부분을 수정해야 하므로 위와 같이 기본 세팅을 해준다
  - 앞으로 이 프로젝트의 모든 유저는 이 모델을 사용하겠다고 정의한 것.
  - get_user_model()은 이 사용자 모델을 불러온다.



#  Models.py

```python
from django.db import models  #기본제공
from django.contrib.auth.models import AbstractUser #참조 사용자 모델 AbstractUser을 불러온다 

class User(AbstractUser):
    address = models.CharField(max_length=100)  
    #  추가하고자 하는 내용이 있다면 작성, 없다면 pass
```

- what is AbstractUser?
  
  - 이를 사용하면 기존의 auth_user 테이블에 있던 열(column)들을 전부 유지한 채 새로운 열을 추가할 수 있다.
  - AbstractBaseUser 상속값 + AbstractUser 상속 값 + 내가 추가로 정의한 값들이 표시된다.
    - ex) name (기본값1)+... +email(기본값2) +... +address(내가 추가한 값)
  
-  `추가할 내용이 없다면 굳이 작성하지 않아도 된다. 단, 나중에 무조건 생기기에 형식은 만든다!`

  

# forms.py

```python
#1 UserCreationForm라는 유저 사용자 폼모델을 상속받아 온다
from django.contrib.auth.forms import UserCreationForm  
#2 get_user_model을 불러온다
from django.contrib.auth import get_user_model  

class CustomUserCreationForm(UserCreationForm):
     #3 이때, 비어있으면 안되는 내용, 검증해야하는 내용은 이 위치에 작성해서 추가검증 대상으로 한다. 
    address = forms.CharField(min_length=3, max_length=99)  

    class Meta:
        #4 model = 사용자모델
        model = get_user_model()  
        #5 모든 내용이 아닌 보이고자 하는 내용만 보여준다
        fields = ('username',)  
      
```

- 사용자모델 forms들을 재정의할 때, Custom을 앞에 붙여준다.
- fields = '' 너무 가져올 게 많으므로, 필요한 것만 fields에 담는다



```python
class CustomUserChangeForm(UserChangeForm):
    address = forms.CharField(min_length=3, max_length=200)
    first_name = forms.CharField(min_length=1, max_length=100)
    last_name = forms.CharField(min_length=1, max_length=100)
    email = forms.EmailField(min_length=1)
    password = None

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'address', 'email', )
```

-  사용자변경모델을 재정의한다 (updata가 없다면 굳이 작성하지 않아도 된다)
- 위와 원리는 동일하다.



# urls.py

```python
생략.
```



# views.py

- 기본세팅

```python
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm #3, 6
from django.contrib.auth import login as auth_login #2
from django.contrib.auth import logout as auth_logout #4
from .forms import CustomUserCreationForm, CustomUserChangeForm #1, 5

# 데코레이터: 로그인이 되었을 때, 어떤 종류의 요청이 들어왔을 때만 함수를 실행하는 데코레이터들
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

# 기본적인 장고 views url
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

#앞으로 사용할 사용자 모델 User를 미리 불러온다
User = get_user_model()  

```

	- 해당 파일이 사용되는 곳에서 다시 표기한다. 이는 단지 모든 import파일을 표시한 것이다.
	- 아래 마지막 줄 return 값들은 가는 방향이 틀릴 수 있으므로 알아서 생각할 것



- index(필요없다면 생략)

```python
def index(request):
    users = User.objects.all()  #유저가 제공하는 모든 정보를 가져온다
    context = {'users': users, }
    return render(request, 'accounts/index.html', context)
```



- signup

```python
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login

def signup(request):
    #1 이미 login한 사용자가 누른다면, `articles:index`로 돌아간다.
    if request.user.is_authenticated: 
        return redirect('articles:index')
	
    if request.method == 'POST':
        #3 만약 post요청(등록)이 들어온다면 요청정보를 담은 CustomUserCreationForm()을 불러온다
        form = CustomUserCreationForm(request.POST)
        
        #4 정보가 유효하다면 정보를 기록하고 로그인해서 profile로 이동한다
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:profile', user.username)
        
    #2 get요청이 들어오면, 비어있는 CustomUserCreationForm() 폼을 가지고 signup.html로 이동한다.
    else:
        form = CustomUserCreationForm()
    context = {'form': form, }
    
    return render(request, 'accounts/signup.html', context)
```

1. `CustomUserCreationForm`은 사용자폼으로 사용자모델에 담긴 내용이 있다.
2. `auth_login(request, user)` : 첫 항은 무조건 request를 받고, 두 번째 항은 사용하는 유저의 정보를 의미한다. 이 때, 아래 login 함수와 이름이 겹치므로 `as`를 이용하여 auth_login으로 이름을 바꿔준다.



- login

```python
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    #2 post요청(login)이 들어오면 정보를 AuthenticationForm에 담아서 가져온다.
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        #3 유효하다면, 로그인한다.
        if form.is_valid():
            auth_login(request, form.get_user())
            #4
            next_url = request.GET.get('next')
            return redirect(next_url or 'articles:index')
    #1 get요청이 온다면,비어있는 AuthenticationForm을 가지고 login.html로 이동한다.
    else:
        form = AuthenticationForm() 
    context = {'form': form, }
    return render(request, 'accounts/login.html', context)
```

1. `AuthenticationForm` : 유저가 존재하는지를 검증하는 Django 내장 모델 폼. 사용자가 로그인 폼에 작성한 정보가 유효한지를 검증함, 빈 폼은 로그인/패스워드 제공



- logout

```python
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')
```

1. `auth_logout`: 내부 캐시등 모든 현재 유저의 로그인 관련 세션을 삭제한다. 

   이 때, 아래 logout 함수와 이름이 겹치므로 `as`를 이용하여 auth_logout으로 이름을 바꿔준다.



- profile

```python
from .forms import CustomUserChangeForm

def profile(request, username): 
    # 유저 정보를 get_object_or_404로 받아온다.
    user = get_object_or_404(User, username=username)
    
    context = {'user_profile': user, }
    
    #사용자와 조회하고자 하는 유저를 비교한다.
    if request.user == user:
        #요청이 post라면, 현재내용을 가진 CustomUserChangeForm을 보여준다.
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=user)
            # 유효하다면, 수정내용을 기록하고 profile페이지로 이동한다.
            if form.is_valid():
                user = form.save()
                return redirect('accounts:profile', username=user.username)
        # get요청이라면,현재 정보를 가지고 form 내용을 가진 수정페이지로 이동한다.
        else:
            form = CustomUserChangeForm(instance=user)
		# form 내용을 context에 추가한다.
        context['form'] = form
    
    #만약 사용자와 조회하고자 하는 유저가 다르다면, 유저의 이름만 보여준다.
    return render(request, 'accounts/profile.html', context)
```

1. `CustomUserChangeForm`은 사용자유저수정폼으로 수정할 때는 변경 내용이 다르므로 이 폼을 따로 사용한다.
2. 수정이므로 마찬가지로 instance항을 이용하여 수정내용을 준비한다.



- change_password

```python
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# 데코레이터: 로그인 상태가 아니면 무시한다
@login_required

def change_password(request):
    #post 요청이라면, passwordform에 담긴 내용을 from에 저장
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        #유효하다면 내용을 저장하고 session을 업데이트해서 로그인을 유지하고 profile 페이지로 반환
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile', form.user.username)
    #get 요청이라면, 비밀번호변경폼을 전달한다.
    else:
        form = PasswordChangeForm(request.user)
    
    context = {'form': form, }
    return render(request, 'accounts/change_password.html', context)
```

1. `PasswordChangeForm `: 비밀번호 변경폼
2. `update_session_auth_hash`: 이 함수는 현재 요청과 새 세션 해시가 파생 될 업데이트 된 사용자 개체를 가져 와서 세션 해시를 적절하게 업데이트합니다. 또한 훔친 세션 쿠키가 무효화되도록 세션 키를 회전합니다.



#  withdraw

```python
@login_required
@require_POST
def withdraw(request):  # 탈퇴
    # 유저를 삭제한다.
    request.user.delete() 
    # cookie(팔찌) 회수 + session 테이블에서 레코드 삭제
    auth_logout(request)  
    return redirect('articles:index')
```





#  html들

 생략! 원리 동일 가끔 if문으로 나눈다!



