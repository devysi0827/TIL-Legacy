#### Date: 1/20

# Today I learned



## 함수 

####              function

### input------------>output

#### - 왜 사용할까요?

-  재사용성 

- 높은 가독성

- 편리한 유지보수

  

#### - 형식 

```python
def <함수이름>(parameter1, parameter2, ......):
    <코드 블럭>
    return value
# 함수이름() or 함수이름(parameter1, ......)로 호출한다
# parameter와 return값은 함수에 따라 있어도 되고 없어도 된다.
# return 값을 만날 경우 함수를 종료하고 호출자리로 돌아가 return값을 반환한다 또한, 단 한개의 객체만 반환되며 기본 return값은 none이다.
# parameter1='기본인자'등으로 기본인자 설정이 가능하다
# 들여쓰기가 어긋날시 오류발생

```



###### 예시

```python
def cube_return(n):
    result = n**3
    return result
```



#### - 성질

- parmeter의 위치에 따라서 입력되는 위치인자이다.
- 기본인자(초기값) 설정이 가능하다.
- 가변 키워드 인자



##  조건문

#### - while

```python
while 조건식:
    명령문1
#따로, 탈출문 제작이 필요
#들여쓰기 조심
```

######  예시

```python
while True:
    print('조건식이 참일 때까지')
    print('계속 반복')
```

### - for

```python
for 임시변수 in 순회가능한데이터(iterable):
    명령문
```

###### 예시

```python
for menu in ['김밥', '햄버거', '피자', '라면']:
    print(menu)
```



####  - pass



#### - continue



#### - break 



```
emurate
```





## 기타

- 

