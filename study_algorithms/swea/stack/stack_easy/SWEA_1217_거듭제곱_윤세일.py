import sys
sys.stdin = open("sample_input.txt","r")

#함수

#본문<-------------------->
case_num = 10  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    trash = input()
    n, m = map(int, input().split( ))
    ans = 1
    for i in range (m):
        ans *= n

    print("#{} {}".format(case+1,ans))