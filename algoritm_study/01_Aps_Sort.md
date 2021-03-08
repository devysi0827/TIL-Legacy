#### Date: none

# Aps Sort



## 정렬
- 값을 순서대로 재배열하는 것
- 종류
  - 버블 정렬
  - 카운팅 정렬
  - 선택 정렬
  - 퀵 정렬
  - 삽입 정렬
  - 병합 정렬



##  버블정렬

- 인접한 두 개의 원소를 비교하면 자리를 계속 교환하는 방식
- 첫 원소부터 인접한 원소를 계속 비교해가며 가장 큰 원소가 마지막자리로 이동한다
- 거품모양과 비슷하다 한다.
- 시간복잡도 = O(n^2)



```python
#버블 정렬
arr = [10, 2, 37, 4, 25]

for i in range(len(arr)-1,0,-1):
    for j in range(0,i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print("#버블 ",end ="")
print(*arr)
```



## 카운팅 정렬

- 항목의 순서를 결정하기 위해 집합에 각 항목이 몇개씩 있는 지 세고 정렬하는 알고리즘
- 정수형 자료형만 분류 가능
- 가장 큰 정수를 알아야만 사용 가능  ->  n이 비교적 작아야만 사용가능, 효율적이다.

- 시간복잡도 = O(n+k)







```python
#카운팅 정렬
arr = [0,1,2,3,3,2,1,2,3,4,3,2,1,2]  #원래배열
answer = ['a']*len(arr)  #반환할 정답배열
max = 0

for ele in arr:  #맥스 구하기
    if max< ele:
        max = ele
count_arr = [0]*(max+1)  #최댓값에 맞는 카운트 배열 생성

for i in range(len(arr)):  #각 숫자 카운트
    count_arr[arr[i]] += 1

for i in range(1,len(count_arr)):  #누적 카운트 함수 만들기
    count_arr[i] += count_arr[i-1]

for i in range(len(answer)-1,-1,-1):  #정답함수에 나열하기
    answer[count_arr[arr[i]]-1] = arr[i]
    count_arr[arr[i]] -= 1

print("#카운팅 ",end ="")
print(*answer)

#아래 방법 중 누적카운트 함수없이 수를 세서 나열하면 더 편하지만 이 방법을 사용시 배열의 순서를 지킬 수 있고, 이를 안정하다 한다.
```



## 셀렉션 알고리즘 & 셀렉션  정렬

- k번째로 큰 또는 작은 원소르 찾는 알고리즘
- 기본적으로 정렬 후 k번째 인덱스를 불러온다.
- 주어진 리스트의 최소값을 선정 맨앞으로 이동, 그 후부터 다시 이 과정을 반복
- 시간복잡도 = O(n^2),  하지만 버블보다 빠르다



```python
#선택정렬 과정
arr = [5,2,6,43,1,6,7]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[j]<arr[i]:
            arr[j],arr[i] = arr[i], arr[j]
```



##  퀵 정렬

- 피벗 기준 작은것은 오른편, 큰 것은 왼편으로 위치시켜서 정렬하는 방법

- 평균 시간복잡도 = O(nlogn)으로 굉장히 빠르지만, 최악의 경우 O(n^2)이다.

```python
def quick_sorted(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)-1]
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
            # print(arr)
        return quick_sorted(left) + mid + quick_sorted(right)
    else:
        return arr


arr = [5,3,8,4,9,1,6,2,7]
print(quick_sorted(arr))
```

