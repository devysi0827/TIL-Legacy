#### Date: 1/20

# Today I learned



## 조건문

#### - 형식 

```python
if 조건 :
    명령문1
else:
    명령문2
# 조건이 참: 명령문 1을 시행 
# *만약 if 1이라면 1은 True임으로 명령문 1이 시행된다! 
# 조건이 거짓: 명령문 2를 시행, else가 없을 시 실행하지 않음
# 들여쓰기가 어긋날시 오류발생

```



###### 예시

```python
if a > 0:
    print('양수입니다.')
else:
    print('음수입니다.')
```



#### - 성질

- 중첩사용이 가능하다
- 조건표현식으로 치환이 가능하다 ex) true_value if <조건식> else false_value



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

