import sys
sys.stdin = open("sample_input (1).txt","r")

#함수
def count_alpa(list_1, alpa):
    count = 0
    for i in list_1:
        if i == alpa:
            count +=1
    return  count


#본문<-------------------->
case_num = int(input())  #최초반복횟수

for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    word = list(input())
    input_list = list(input())
    max_alpa =0
    for i in range(len(word)):
        alpa_count = count_alpa(input_list, word[i])
        if alpa_count > max_alpa:
            max_alpa = alpa_count
    print("#{} {}".format(case + 1, max_alpa))

