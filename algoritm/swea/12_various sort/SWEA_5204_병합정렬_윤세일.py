import sys
sys.stdin = open("1.txt","r")

def merge_sort(list_1):
    if len(list_1) == 1:
        return list_1
    left = []
    right = []
    mid = int(len(list_1)/2)
    for i in range(mid):
        left.append(list_1[i])
    for i in range(mid,len(list_1)):
        right.append(list_1[i])
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    global cnt
    idx_l =0
    idx_r = 0
    result = []
    if left[-1] > right[-1]:
        cnt += 1

    while idx_l < len(left) or idx_r < len(right):
        if idx_l < len(left) and idx_r < len(right):
            if left[idx_l] <= right[idx_r]:
                result.append(left[idx_l])
                idx_l +=1
            else:
                result.append(right[idx_r])
                idx_r+=1
        elif idx_l < len(left):
            result.append(left[idx_l])
            idx_l += 1
        elif idx_r < len(right):
            result.append(right[idx_r])
            idx_r += 1
    return  result

tcs = int(input())
for tc in range(tcs):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    a = merge_sort(arr)
    print("#{} {} {}".format(tc + 1, a[int(n//2)], cnt))

