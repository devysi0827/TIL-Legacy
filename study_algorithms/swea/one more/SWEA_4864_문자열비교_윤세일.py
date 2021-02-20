import sys
sys.stdin = open("sample_input.txt","r")
case_num = int(input())  #최초반복횟수
#함수
#본문
for case in range(case_num):

    word = list(input())
    input_list= list(input())
    check = 0

    for i in range(len(input_list)-len(word)+1):
        if word[0] == input_list[i]:
            for j in range(len(word)):
                if word[j] == input_list[i+j]:
                    check = 1
                else:
                    check = 0
                    break
        if check == 1:
            break


    print("#{} {}".format(case+1, check))
    # print(*answer_list)












