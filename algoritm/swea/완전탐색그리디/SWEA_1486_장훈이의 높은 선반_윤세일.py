import sys

sys.stdin = open("sample_input (5).txt","r")

T = int(input())

for tc in range(T):
    # 기본 세팅
    n, m = map(int,input().split())
    clerks = list(map(int,input().split()))
    min_sum = 99999999

    for i in range(1 << n):
        list_sum = 0

        for j in range(n + 1):
            if i & (1 << j):
                list_sum += clerks[j]
                if list_sum > min_sum :
                    break

        if list_sum >= m:
            ans = list_sum
            min_sum = list_sum


    print("#{} {}".format(tc+ 1, min_sum-m))




