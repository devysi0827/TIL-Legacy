# #순열 6_P_3
# arr = [1,2,3,4,5]
# for i in range(1,6):
#     for j in range(1,6):
#         if j !=i:
#             for k in range(1,6):
#                 if k != i and k !=j:
#                     pass
#                     print("#순열")
#                     print("{} {} {}".format(i,j,k))
#
#
# #버블 정렬
# arr = [10, 2, 37, 4, 25]
#
# for i in range(len(arr)-1,0,-1):
#     for j in range(0,i):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#
# print("#버블 ",end ="")
# print(*arr)
#
# #카운팅 정렬
# arr = [0,1,2,3,3,2,1,2,3,4,3,2,1,2]  #원래배열
# answer = ['a']*len(arr)  #반환할 정답배열
# max = 0
#
# for ele in arr:  #맥스 구하기
#     if max< ele:
#         max = ele
# count_arr = [0]*(max+1)  #최댓값에 맞는 카운트 배열 생성
#
# for i in range(len(arr)):  #각 숫자 카운트
#     count_arr[arr[i]] += 1
#
# for i in range(1,len(count_arr)):  #누적 카운트 함수 만들기
#     count_arr[i] += count_arr[i-1]
#
# for i in range(len(answer)-1,-1,-1):  #정답함수에 나열하기
#     answer[count_arr[arr[i]]-1] = arr[i]
#     count_arr[arr[i]] -= 1
#
# print("#카운팅 ",end ="")
# print(*answer)
#
# #배열 순회: 행 우선 순회
# arr = [[1,2,3,4], ['a','b','c','d'], ['ㄱ', 'ㄴ', 'ㄷ','ㄹ'],['+','-','*','/']]
# print("#행")
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         pass
#         print(arr[i][j], end="")
#
# #배열 순회: 열 우선 순회
# print()
# print('#열')
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         pass
#         print(arr[j][i], end ="")
#
# #배열 순회: 지그재그 순회
# print()
# print('#지그재그')
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         pass
#         if i%2 ==0:
#             print(arr[i][j], end ='')
#         else:
#             print(arr[i][len(arr)-j-1], end ='')
#
# #델타
# arr =[[1,2,3],[4,5,6],[7,8,9]]
# row=1
# col=1
# print('#현재위치 {}'.format(arr[row][col]))  #현재좌표에 위치(기준)
# dr =[1,-1,0,0]  #열로 읽으면 [[1,0], [-1,0], [0,1], [0,-1]] 이다.
# dc =[0,0,1,-1]
# for i in range(4):
#     row_move = row+dr[i]
#     col_move = col+dc[i]
#     print('#이동위치 {}번째 {} '.format(i, arr[row_move][col_move]))  #기준좌표에서 dr , dc만큼 이동
#
# #전치행렬
# arr =[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(3):
#     for j in range(3):
#         if i<j:
#             arr[i][j], arr[j][i] = arr[j][i],arr[i][j]
# print(arr)
#
# #부분집합
# arr = [3,6,1,7,5,8]
# n=len(arr)
#
# for i in range(1<<n):
#     for j in range(n+1):
#         if i & 1<<j:
#             print(arr[j], end=',')
#     print()
# print()

# #정렬 되어있는 이진검색
# find = 55
# start =1
# end = 100
# numbers =[]
# for i in range(1,101):  #숫자배열 만들기
#     numbers.append(i)
#
# num = 0  #반복횟수
# while start < end:
#     num += 1
#     middle = int((start+end)/2)
#     if middle == find:
#         print('#반복횟수:{}, 찾았다'.format(num))
#         break
#     elif middle < find:
#         start = middle
#     else:
#         end = middle
#
# else:
#     print('실패')

# #선택정렬 과정
# arr = [5,2,6,43,1,6,7]
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         if arr[j]<arr[i]:
#             arr[j],arr[i] = arr[i], arr[j]

# atoi, itoa (생략)

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


