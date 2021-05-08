import sys
sys.stdin = open("1.txt","r")

def hor_sort(arr,l,r):
    fir_idx = l+1
    end_idx = r  # len(arr) - 1
    pivot = arr[l]
    check = 0
    while fir_idx <= end_idx:
        if check == 1:
            break
        if fir_idx == end_idx:
            check=1
        while arr[fir_idx] <= pivot:
            if fir_idx == len(arr)-1:
                break
            fir_idx += 1

        while arr[end_idx] > pivot :
            if end_idx == 0:
                break
            end_idx -= 1

        if fir_idx < end_idx:
            arr[fir_idx], arr[end_idx] = arr[end_idx], arr[fir_idx]


    arr[end_idx], arr[l] = arr[l], arr[end_idx]
    return end_idx

def quick_sort(arr, l, r):
    if l < r:
        s = hor_sort(arr, l, r)
        quick_sort(arr, l, s-1)  # 피봇 기준 왼쪽 정렬
        quick_sort(arr, s + 1, r)  # 피봇 기준 오른쪽 정렬

tcs = int(input())
for tc in range(tcs):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    quick_sort(arr, 0, len(arr) - 1)
    print("#{} {}".format(tc + 1, arr[int(n//2)]))
#
# arr = [3,2,4,6,9,1,8,7,5]
# quick_sort(arr,0,len(arr)-1)
# print(arr)
