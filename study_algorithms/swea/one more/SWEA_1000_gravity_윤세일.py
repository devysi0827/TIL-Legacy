# 3
# 9
# 7 4 2 0 0 6 0 7 0
# 9
# 7 4 2 0 0 6 7 7 0
# 20
# 52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
#
# #1 7
#
# #2 6
#
# #3 13

import sys

sys.stdin = open("input.txt","r")

test_case = int(input())
for case in range(test_case):
    input_num = int(input())
    input_str = input()
    input_list = list(map(int,input_str.split()))
    maximum = 0
    max_count = 0

    for number in input_list:
        if number > maximum:
            maximum = number  #가장 큰 수를 찾는다.

    for i in range(1, maximum+1):
        count = 0
        minus_count = 0
        for input_number in input_list:
            if input_number >= i:
                count += 1  #빈공간을 센다
            if count == 0:
                minus_count +=1  #왼쪽 빈공간을 센다
        if input_num - count -minus_count > max_count: #블록수 = 전체길이 - 빈공간 - 왼쪽 빈공간
            max_count = input_num - count - minus_count

    print("#%d %d"%(case+1, max_count))

























# test_case = 3
# for case in range(test_case):
#     input_num = int(input())
#     input_str = input()
#     input_list = list(map(int,input_str.split()))
#     max_fall = 0
#     fall_block = 0
#     for input_number in range(len(input_list)) :
#         for input_number_2 in range(len(input_list)):
#             if input_number < input_number_2 and input_list[input_number] - input_list[input_number_2] >= max_fall :
#                 max_fall = input_list[input_number] - input_list[input_number_2]
#                 fall_number = input_number_2
#
#
#
#     print(max_fall-(input_num - fall_block - 1))


