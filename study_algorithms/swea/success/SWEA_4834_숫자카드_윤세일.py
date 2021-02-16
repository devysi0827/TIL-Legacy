import sys

sys.stdin = open("input.txt","r")
# input
# 3
# 5
# 49679
# 5
# 08271
# 10
# 7797946543
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
    input_list = list(map(int,input()))

    number_list = [0]*10
    for number in input_list:
        number_list[number] +=1

    max_index = 0
    index_number = -1
    for index in range(len(number_list)):
        if max_index < number_list[index]:
            max_index= number_list[index]
            index_number = index

        if max_index == number_list[index] and index_number< index:
            index_number = index

    print("#%d %d %d"%(case+1, index_number, max_index))


