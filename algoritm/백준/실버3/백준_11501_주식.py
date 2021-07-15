import sys
sys.stdin = open("1.txt", "r")

repeat_num = int(input())
for i in range(repeat_num):
    n = int(input())
    arr = list(map(int,input().split()))
    # print(arr)
    ans = 0
    start = arr[n-1]
    for j in range(n-1,-1,-1):
        if arr[j] <start:
            ans += start -arr[j]
        elif arr[j] > start:
            start = arr[j]
    print(ans)







