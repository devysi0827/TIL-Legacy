# 1st week (1/18-1/22)



## 자주 쓰는 연산자

- \n : 줄바꿈
- \t : 텝
- / : 나눗셈 , // : 몫, % : 나머지, ** : 제곱
- in & not in : 포함여부 확인



## 변경 가능, 불가능

- 변경 가능한 것(`mutable`) : list, dict, set

 - 변경 불가능한 것(`immutable`): 리터럴(literal), 숫자(Number), 글자(String), 참/거짓(Bool), range(), tuple()

  

## 알아두면 좋은 것들

- concatenation : 문자열, 숫자 각각은 합성이 된다.

  ```python
a1 = 'a' 
b1 = 'b'
ab = a1 + b1  # ab = 'ab'
  ```

- slicing : 특정 범위의 문자열과 리스트를 뽑을 수 있다.

  ```python
  l= [1, 2, 3, 4]
  s= 'lkjhg'
  print(l[0:2]) #[1, 2]
  print(s[:-1]) #lkjh
  ```

- 형변환

	```python
list(), str(), int(), float()
	```
	
- 기타

	```python
test.split(',')  #''안에 문자로 문자열을 나누어준다. ex) '3,4' => '3' , '4'
	test =':'.join(list) #list값을 ''로 구분하여 문자열로 더해준다. ex)[3, 4] => '3:4'
	test.strip('a')  #''값을 문자열에서 제거
	set()  #중복제거
	ord(), chr()  #문자를 아스키코드숫자로 아스키코드 숫자를 문자로 바꿔주는 함수
	input()  #입력함수
	```



##  자주 보는 에러 모음

주로 대/ 소문자의 구분, 들여쓰기 ,스펠링 오류

- syntax error :문법 확인할 것

- EOL : 문장이 끝났는지 확인할 것  주로 괄호 오류

- 'x' is not defined : 'x'변수가 없다

  

##  출력방법

````python
print('Hello, %s, %d' % (name, score))

print('Hello, {}. 내 성적은 {}'.format(name, score))

print(f'Hello, {name}. 내 성적은 {score}. {score}지롱!')

print('', end='')  #붙여쓰기 한칸 뛰우기 등등 가능
````



## list 정리

- 리스트 추가

```python
list_test += [1]  #int형 
list_test += '2'  #str형
list_test += [[3]]  #list형

list_test.append(dicto) #dict는 이형태로 안되며 append를 써야 한다.
list_test.assert(2,'ssafy')  # [2]번 위치에 'ssafy'를 추가

print (list_test) #[1, '2', 'ssafy', [3], {0: '10'}]
```

- 리스트 변경

```python
list_test[0] = 'change'  #리스트[위치] = 내용
list_test.remove([3])  # ()안에 값 삭제, 가장 앞에 하나만 삭제
del list_test[1]  #리스트[1]번 항 삭제
```

- 리스트 정리

```python
list_test = [1, 2, 3, 4, 5, 4]

list_test.sort() #정렬 [1, 2, 3, 4, 4, 5], 자동으로 list의 반영
list_test.reverse() #뒤집기 [5, 4, 4, 3, 2, 1], 자동으로 list의 반영
list_data[::-1] #뒤집기2 [1, 2, 3, 4, 4, 5], 리스트의 자동반영 되지 않음 따로 저장 필요
list_data.count(4) #괄호안 요소 세기, 4, 리스트의 자동반영 되지 않음 따로 저장 필요
```



## dict 정리

- dic 추가하는 법

```python
dic = { }
dic['a'] =1 #dic 추가법(생성) {'a': 1}
```

- dic 읽는 법

```python
dic = {'key1' : 1, 'key2' : 2, 'key3' : 3}
dic['key1']  # 1, dic[접근하는 키의 이름]
dic.get('key1')  #1, dic.get(접근하는 키의 이름)
dic.keys()  #dict_keys(['key1', 'key2', 'key3']),  key들(사용하려면 list 변환 필요)
dic.values()  #dict_values([1, 2, 3]),  value들(사용하려면 list 변환 필요)
dic.items()  #dict_items([('key1', 1), ('key2', 2), ('key3', 3)])
```



## 기타

- 조건표현식으로 치환이 가능하다  ex) true_value if <조건식> else false_value
- enumerate를 이용해 리스트에 인덱스와 값을 동시에 표현할 수 있다.
- 이름 검색 규칙 local < enclosed < global < bulit-in
- 재귀함수는 베이스(끝)이 필요하다.
- 함수는 위치인자, 가변키워드 인자가 있다.
- for- else문도 존재한다.

