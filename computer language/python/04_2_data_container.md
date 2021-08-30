#### Date: 1/18

# Today I learned



## 시퀸스형

###  - 특징 

- 순서가 있다
- 특정 위치의 데이터를 가리킬 수 있다.
- 리스트, 튜플, 레인지, 문자형(str), 바이너리(다루지 않음) 가 있다



### - 시퀸스 함수

|    operation |                    설명 |
| -----------: | ----------------------: |
|     x `in` s |        containment test |
| x `not in` s |        containment test |
|    s1 `+` s2 |           concatenation |
|      s `*` n | n번만큼 반복하여 더하기 |
|       `s[i]` |                indexing |
|     `s[i:j]` |                 slicing |
|   `s[i:j:k`] |       k간격으로 slicing |
|       len(s) |                    길이 |
|       min(s) |                  최솟값 |
|       max(s) |                  최댓값 |
|   s.count(x) |                x의 개수 |



## 비시퀸스형 

### - 특징 

- 순서가 없다(사용시 무작위로 재배치될 수 있다)
- set, dictionary

### - set

-  중복허용을 하지 않는다

- {}로 구분하나, 빈 set은 set()으로 만든다

### - dictionary

- key와 value가 합쳐져서 존재한다, 두 개를 합쳐서 item 이라 한다
- dict(), dict{} 모두 빈 dictionary 생성가능
- `key`는 변경 불가능한 데이터, `value`는 list, dictionary 모두 포함 가능하다.



##  형변환표

![typecasting](https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png)

  ## 데이터분류 

변경 가능한 것(`mutable`)들과 변경 불가능한 것(`immutable`)로 나누어짐



###  - 변경 가능한 것(`mutable`)

`list`, `dict`, `set`



###  - 변경 불가능한 것(`immutable`)

리터럴(literal), 숫자(Number), 글자(String), 참/거짓(Bool), range(), tuple(), frozenset()



###  - 변경 가능하다?

변경 가능: 데이터 저장위치(주소)를 그대로, 데이터를 추가할 수 있다.

변경 불가능: 데이터를 수정할 수 없어서 수정한 데이터를 새로 메모리의 할당하고 그 쪽으로 변수를 재할당한다. 

(즉, 포인터를 변경할 뿐이지 데이터를 바꿀수는 없다.

)

## 정리 



![container](https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png)





