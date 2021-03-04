import sys
sys.stdin = open("2.txt","r")

#함수

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    numbers =[2,3,5,7,11]
    answer = []
    for number in numbers:
        count = 0
        while n % number == 0:
            n = n /number
            count +=1
        answer.append(count)
    print("#{} ".format(case + 1), end="")
    print(*answer)