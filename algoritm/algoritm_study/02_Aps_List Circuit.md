#### Date: none

# Aps List Circuit 



## 기본 행렬 순회

- 행 우선순회
- 열 우선순회
- 지그재그 순회
- 전치 행렬



```python

#배열 순회: 행 우선 순회
arr = [[1,2,3,4], ['a','b','c','d'], ['ㄱ', 'ㄴ', 'ㄷ','ㄹ'],['+','-','*','/']]
print("#행")
for i in range(len(arr)):
    for j in range(len(arr)):
        pass
        print(arr[i][j], end="")

#배열 순회: 열 우선 순회
print()
print('#열')
for i in range(len(arr)):
    for j in range(len(arr)):
        pass
        print(arr[j][i], end ="")

#배열 순회: 지그재그 순회
print()
print('#지그재그')
for i in range(len(arr)):
    for j in range(len(arr)):
        pass
        if i%2 ==0:
            print(arr[i][j], end ='')
        else:
            print(arr[i][len(arr)-j-1], end ='')

#전치행렬
arr =[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        if i<j:
            arr[i][j], arr[j][i] = arr[j][i],arr[i][j]
print(arr)
```





##   델타 

- 2차원 배열의 한 좌표에서 인접 배열 요소를 탐색하는 방법



```python
#델타
arr =[[1,2,3],[4,5,6],[7,8,9]]
row=1
col=1
print('#현재위치 {}'.format(arr[row][col]))  #현재좌표에 위치(기준)
dr =[1,-1,0,0]  #열로 읽으면 [[1,0], [-1,0], [0,1], [0,-1]] 이다.
dc =[0,0,1,-1]
for i in range(4):
    row_move = row+dr[i]
    col_move = col+dc[i]
    print('#이동위치 {}번째 {} '.format(i, arr[row_move][col_move]))  #기준좌표에서 dr , dc만큼 이동
```




##     부분집합 생성

-  각 i 번째 원소가 들어있는 지 체크하며 포함여부를 반복하면 부분집합이 된다



```python
#부분집합
arr = [3,6,1,7,5,8]
n=len(arr)

for i in range(1<<n):
    for j in range(n+1):
        if i & 1<<j:
            print(arr[j], end=',')
    print()
print()ㅔ
```




## 검색

- 순차검색 
  - 순서대로 필요한 자료가 있는 지 검색하는 방법, 굉장히 편하나 굉장히 비효율적
  - 찾고자 하는 원소의 순서에 따라서,  효율성이 달라져 안정적이지 못하다(비정렬식 = O(n))
  - 위와 같은 문제점은 정렬되어 있으면 극복할 수 있다.(정렬식 = O(n),  단 비정렬식보다 평균 두배차이가 난다)
- 이진검색
  - 정렬되어 있을때만 가능하다
  - 반을 나누어서 시작점과 종료점을 바꾸며 검색을 반복 수행한다.



```python
#정렬 되어있는 이진검색
find = 55
start =1
end = 100
numbers =[]
for i in range(1,101):  #숫자배열 만들기
    numbers.append(i)

num = 0  #반복횟수
while start < end:
    num += 1
    middle = int((start+end)/2)
    if middle == find:
        print('#반복횟수:{}, 찾았다'.format(num))
        break
    elif middle < find:
        start = middle
    else:
        end = middle

else:
    print('실패')
```