import sys
sys.stdin = open("sample_input.txt","r")

#함수

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    word = list(map(int,input()))
    count = 0
    error_mermory = [0]*len(word)

    for i in range(len(word)):
        if count%2 ==0:
            if word[i] != error_mermory[i]:
                count +=1
                continue
        if count%2 ==1:
            if word[i] == error_mermory[i]:
                count +=1


    print("#{} {}".format(case+1,count))