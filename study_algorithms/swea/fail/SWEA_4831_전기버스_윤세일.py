import sys
sys.stdin = open("sample_input.txt","r")

#함수


#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    k, n, m = map(int,input().split( ))
    charge = list(map(int,input().split( )))
    charge = [0]+ charge +[n]
    last = 0

    for i in range(1,m+2):
        if charge[i] -charge[i-1] > k:
            ans = 0
            break

        if charge[i] > last +k:
            last = charge[i-1]
            ans +=1

    # for i in charge:
    #     stops[i] = 1
    # print(stops)
    # bus = 0
    # ans = 0
    #
    # while 1:
    #     bus +=k
    #     if bus >= n:
    #         break
    #
    #     for i in range(bus, bus -k, -1):
    #         if stops[i]:
    #             ans +=1
    #             bus = i
    #             break
    #     else:
    #         ans = 0
    #         break

    print("#{} {}".format(case+1,ans))