import sys
sys.stdin = open("1.txt","r")

money =[50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for tc in range(T):
    # 기본 세팅
    ans_list = [0]* 8
    n = int(input())
    for i in range(8):
        gijoon = money[i]
        if n%gijoon == n:
            continue
        else:
            ans_list[i] += int(n//gijoon)
            n = n - money[i] * int(n//gijoon)
        if n == 0:
            break

    print('#{}'.format(tc + 1))
    print(*ans_list)