import sys
sys.stdin = open("1.txt","r")

repeat = int(input())
for i in range(repeat):
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(list(map(int,input().split())))
    arr = sorted(arr,reverse=True)
    # print(arr)

    count = 1
    my_num = arr[n-1][1]
    for j in range(n-2,-1,-1):
        if arr[j][1] < my_num:
            my_num = arr[j][1]
            count +=1
    print(count)








