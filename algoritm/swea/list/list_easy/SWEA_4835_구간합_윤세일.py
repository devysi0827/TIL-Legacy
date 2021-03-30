import sys
#input
# 3
# 10 3
# 1 2 3 4 5 6 7 8 9 10
# 10 5
# 6262 6004 1801 7660 7919 1280 525 9798 5134 1821
# 20 19
# 3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176
sys.stdin = open("input.txt","r")

test_case = int(input())

def inteval_sum(now, interval, list_a):
    ans = 0
    for i in range(interval):
        ans += list_a[now+i]
    return  ans

for case in range(test_case):
    input_num_and_interval = list(map(int,input().split()))
    input_num = input_num_and_interval[0]
    input_interval = input_num_and_interval[1]
    input_list = list(map(int,input().split()))  #입력 받기

    min_sum = inteval_sum(0, input_interval, input_list)
    max_sum = 0

    for repeat in range(len(input_list)-input_interval+1):
        inter_sum = inteval_sum(repeat, input_interval, input_list)
        if max_sum < inter_sum:
            max_sum = inter_sum
        if min_sum > inter_sum:
            min_sum = inter_sum

    print(max_sum-min_sum)






















#
# def interval_sum(a, b, list_a):
#     interval_sum = 0
#     for i in range(a) :
#         interval_sum += list_a[i+b]
#     return interval_sum
#
# for case in range(test_case):
#     input_num_and_interval = list(map(int,input().split()))
#     input_num = input_num_and_interval[0]
#     input_interval = input_num_and_interval[1]
#     input_str = input()
#     input_list = list(map(int,input_str.split()))
#     min_sum = 0
#     max_sum = 0
#
#     for i in range(input_num-input_interval):
#         inter_sum = interval_sum(input_interval, i, input_list)
#         if max_sum < inter_sum:
#             max_sum = inter_sum
#         if min_sum > inter_sum:
#             min_sum = inter_sum
#
#     print(max_sum-min_sum)