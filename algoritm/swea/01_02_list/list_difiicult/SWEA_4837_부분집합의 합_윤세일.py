#  입력
import sys
sys.stdin = open("sample_input (3).txt","r")
case_num = int(input())  #최초반복횟수

answer = 0
numbers = []
for i in range(12):
    numbers.append(i+1)
number = len(numbers)

for case in range(case_num):
    n, sum_n =  map(int,input().split())
    answer =0
    for i in range(1<<number):
        list_sum = 0
        list_n =0
        for j in range(number+1):
            if i & (1<<j):
                list_sum+= numbers[j]
                list_n +=1
        if list_sum == sum_n and list_n == n:
            answer +=1

    print(answer)
# n = len(arr)
#
# for i in range(1 << n):
#     sum_list = []
#     sum_num = 0
#     for j in range(n + 1):
#         if i & (1 << j):
#             sum_list.append(arr[j])
#             sum_num += arr[j]
#
#     if sum_num == 10:
#         for k in range(len(sum_list)):
#             print(sum_list[k], end = ',')
#         print()