import sys
sys.stdin = open("GNS_test_input (1).txt","r")
case_num = int(input())  #최초반복횟수
#함수
def count_word(list_1,word):
    count =0
    for i in list_1:
        if i == word:
            count +=1
    return count
#본문
for case in range(case_num):
    trash = input()
    input_list= list(input().split( ))
    my_str = [ "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    numbers = [0]*10

    for i in range(len(my_str)):
        numbers[i] = count_word(input_list,my_str[i])

    answer_list = []
    for i in range(len(my_str)):
        for j in range(numbers[i]):
            answer_list.append(my_str[i])

    print("#{}".format(case+1))
    print(*answer_list)


















    # input_number_list = []
    # for i in input_list:
    #     for j in range(len(my_str)):
    #         if i == my_str[j]:
    #             input_number_list.append(j)
    #
    #
    # for i in range(len(input_number_list)):
    #     for j in range(len(input_number_list)):
    #         if i<j and input_number_list[i]>input_number_list[j]:
    #             input_number_list[i],input_number_list[j] = input_number_list[j], input_number_list[i]
    #
    # numbers = [0,1,2,3,4,5,6,7,8,9]
    # answer_list = []
    # for i in input_number_list:
    #     for j in range(len(numbers)):
    #         if i == numbers[j]:
    #             answer_list.append(my_str[j])
    # print("#{}".format(case+1), end="")
    # print(*answer_list)
