#### Date: none

# Aps String



## 문자열을 뒤집는 다양한 방법들

```python
s = 'reverse the strings'
#1 슬라이싱으로 뒤집어 출력
s= s[::-1]
print(s)
#2 반복문으로 뒤부터 새 문자열의 삽입
s= list(s)
reverses = ''
for i in range(len(s)-1,-1,-1):
    reverses += s[i]
print(reverses)
#3 앞과 뒤 문자를 바꾸기
for i in range(len(s)//2):
    s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
print(s)
```



##  문자와 숫자 교환

- 동일 문자 확인을 위해서는 == 연산자와 is 연산자 사용
- atoi() 와 itoa()가 존재한다

```python
def itoa(n):

    my_str = ''
    if n<0:
        n= -n
        my_str ='-'
        
        # 리스트로 나누기
    my_list = []
    while 1:
        my_list.append(n%10)
        n = n//10
        if n<10:
            my_list.append(n)
            break

        #문자화
    zero = ord("0")
    for i in range(len(my_list)-1,-1,-1):
        my_str += chr(my_list[i]+zero)

    return my_str

a = itoa(368)
b = itoa(-17)
print(type(a),a)
print(type(b),b)

```



##  고지식한 알고리즘

- 본문 문자열을 처음부터 끝까지 순회하면서 패턴 내 문자들을 일일이 비교하는 방식
- 이를 줄일 수 있는가?
- 시간복잡도 O(mn)



```python
#brute force
sentence = 'banana apple iphone'
word = 'apple'
i=0
j=0

while j< len(word) and i< len(sentence):
    if sentence[i] != word[j]:
        i =i-j
        j=-1
    i=i+1
    j=j+1
if j==len(word) :
    print(i - len(word))
else:
    print('실패')
```



##  다양한 패칭매턴 알고리즘

- 카프-라빈 알고리즘
  - 불일치가 발생한 앞부분은 무시하고 다시 비교
  - 시간복잡도 = O(M+N),  O(N)?
- KMP 알고리즘
  - 일치하는 패턴이 될때까지 단어 길이만큼 점프
  - 대다수의 소프트웨어가 채택중
  - 시간복잡도 = O(N)
- 보이어-무어 알고리즘
  - 패턴의 오른쪽부터 비교하여 모든 문자를 살피지 않고 이동한다. (APPLE에서 E가 기준)
  - 시간복잡도 = O(M+N)



이 내용들은 아직 상세히 다루지 않는다