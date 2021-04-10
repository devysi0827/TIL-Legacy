# CT 과제

### 시간복잡도

1.

```
T(n) = T(n-1)+n
T(n-1) = T(n-2)+n-1
T(n-2) = T(n-3)+n-2
......
T(2) = T(1)+2
모든 항을 더해서 중복값을 지워주면,
-----------------------
T(n) = T(1)+2+3+.....+n-1+n = T(1)+n*(n-1)/2
T(n) = O(n^2)
```

2.

```
T(n) = T(n/2)+1
T(n/2) = T(n/4)+1
T(n/4) = T(n/8)+1
......
T(2) = T(1)+1
모든 항을 더해서 중복값을 지워주면,
if n = 2^k, k=log(n)
-----------------------
T(n) = T(1)+log(n)
T(n) = O(log(n))
```

3.

```
T(n) = 2T(n/2)+n
T(n/2) = 2T(n/4)+n/2
T(n/4) = 2T(n/8)+n/4
......
T(2) = T(1)+2
위 값을 재귀처럼 타고 올라가면
if n = 2^k, k=log(n)
-----------------------
T(n) = (2^k) * T(n/(2^k))+k*n
	 = n*T(1) + log(n)*n
	 n* T(1)은 일차항이므로, 무시하면
T(n) = O(nlog(n))
```

4.

```
T(n) = T(n-1)+1/n
T(n-1) = T(n-2)+1/(n-1)
T(n-2) = T(n-3)+1/(n-2)
......
T(2) = T(1)+1/2
모든 항을 더해서 중복값을 지워주면,
-----------------------
T(n) = T(1)+1/2+1/3+.....+ 1/(n-1)+ 1/n
식 8-1을 사용하여 치환하면,
T(n) = T(1)+(log(n)-log(2))-1
T(n) = O(log(n))
```

  ![img](컴퓨팅사고력_1_윤세일.assets/DRW000058a840ed.gif)  ..... 식 8-(1)



### MERGE SORT

1. 수도코드

```
def merge_sort(list_1):
	if len(list_1) ==1: return list_1
	
	left = []
	right = []
	mid = len(list_1)/2
	for x in m before mid:
		add x in left
	for x in m after or equal mid:
		add x in right
		
	merge_sort(left)
	merge_sort(right)
	
	return merge(left, right)
	
def merge(left, right):
	answer = []
	idx_l = 0
	idx_r = 0
	
	while idx_l < len(left) or idx_r < len(right):
		if idx_l < len(left) and idx_r < len(right):
			if left[idx_l] <= right[idx_r]:
				answer.append(left[idx_l])
			else:
				answer.append(right[idx_l])
		
		elif: idx_l < len(left):
        	answer.append(left[idx_l])
		else:
			answer.append(right[idx_r])
	return answer
	
```



2. 정확성 증명

```
1. merge_sort(list_1)에서 list_1의 길이가 1일때,
if len(list_1) ==1:
	merge_sort return list_1 #길이가 하나라 정렬할 필요가 없음

it's ok

2. merge_sort(list_1)에서 list_1의 길이가 n일때,
	if len(list_1) == n:
	merge_sort(list_1) : first, len == n 
	merge_sort(left) : second, len ==n/2 
	merge_sort(left) : 3, len == n/4
	......
	merge_sort(left) : 2^(log(n))-1, len == 2
	merge_sort(left) : 2^(log(n)), len == 1 -> return left
	merge_sort(right) : len == 2 -> return
	merge(left, right) : # len == 2 -> return 정렬값
		# 두 원소를 비교하여 작은 값을 넣는다.
		if idx_l < len(left) and idx_r < len(right):
            if left[idx_l] <= right[idx_r]:
                    answer.append(left[idx_l])
                    #left의 원소가 작으면 left를 먼저넌다.
                else:
                    answer.append(right[idx_l])
                    #right의 원소가 작으면 right를 먼저넌다.
		# left나 right 한쪽에만 남으면 그 원소를 모두 추가한다.
		elif: idx_l < len(left):
        	answer.append(left[idx_l])
		else:
			answer.append(right[idx_r])
			
		
	merge(right) : 2^(log(n))-1, len == 2
	merge(left,right) : len == 2 -> return 정렬값
	merge(left,right) : len == 4 -> return 정렬값
	......
	merge(left,right) : len == n -> return 정렬값

따라서 n일때도 return 되는 값이 정렬된 리스트임을 알 수 있다.
	

```



3. 시간복잡도

```
T(n)에 대허서 1회 실행할때마다 반씩 갈라져서 횟수가 증가하므로 
T(n) = 2T(n/2)+b의 관계가 있음을 알 수 있다.
이 때, b는 매 회 , n회씩 해당 점화식의 길이만큼(우연의 일치로 이 경우 T(1)=1로 하면 N=길이가 성립)
조회가 실행되므로,
T(n) = 2T(n/2)+n 이다.
```





### 동적프로그래밍

1-1.

```
피보나치 수열 수도코드
fibo(n) {
	if(n<=2) return 1
	return fibo(n-1)+ fibo(n-2)
}
```



```
1.
n=1 or n=2
fibo(1) =1, fibo(2) =1이므로 위가 성립한다.

2. 
n=k일때,
fibo(k) = fibo(k-1) +fibo(k-2)로 성립한다.

```

```
시간복잡도
T(n) = 2T(n-1)
T(n-1) = 2T(n-2)
T(2) = 2T(1)
위 식을 모두 곱하면
----------
T(n) = 2^(n-1)*T(1)
T(n) = O(2^n)
```





2.(과제)

```
피보나치 수열 수도코드
fibo(n) {
	if(n<=2) return 1
	return fibo(n-1)+ fibo(n-2)
}
```

```
1.
n=1 or n=2
fibo(1) =1, fibo(2) =1이므로 위가 성립한다.

2. 
n=k일때,
fibo(k) = fibo(k-1) +fibo(k-2)로 성립한다.

```

```
이 식은 미리 저장된 캐시값에 현재값을 더하기만 하면 되므로
T(N) = T(N-1)+1
T(N-1) = T(N-2)+1
T(2) = T(1)+1
----------------
T(N) = T(1)+N-1
T(N) = N
```



