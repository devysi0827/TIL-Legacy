import sys
sys.stdin = open("sample_input (1).txt","r")

#함수


#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    senten, word = input().split( )
    senten = list(senten)
    answer = 0
    i=0
    while i< len(senten):
        if i< len(senten)-len(word)+1:
            check = True
            if word[0] == senten[i]:
                for j in range(1,len(word)):
                    if word[j] != senten[j+i]:
                        check = False
                        break
                if check == True:
                    i += len(word)-1

        answer +=1
        i +=1

    print('#{} {}'.format(case + 1, answer))

