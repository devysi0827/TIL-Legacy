import sys

sys.stdin = open("input.txt","r")
#input
# 3
# 5
# 477162 658880 751280 927930 297191
# 5
# 565469 851600 460874 148692 111090
# 10
# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
def list_max(list_a):
    max = 0
    min = list_a[0]
    for a in list_a :
        if a> max :
            max =a
        if a< min :
            min = a

    return max-min

test_case = int(input())

for case in range(test_case):
    input_num = int(input())
    input_str = input()
    input_list = list(map(int,input_str.split()))

    maximum = list_max(input_list)
    print("#%d %d"%(case+1, maximum))
























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


