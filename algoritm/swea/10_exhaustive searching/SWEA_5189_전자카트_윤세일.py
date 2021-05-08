import sys, copy
sys.stdin = open("1.txt","r")

def perm(idx):
    # 다 뽑아서 정리했다면
    if idx == N:
        perm_list.append([0]+sel+[0])
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]  # 값을 써라
                check[i] = 1  # 사용을 했다는 표시
                perm(idx+1)
                check[i] = 0  # 다음 반복문을 위한 원상복구


T = int(input())

for tc in range(T):
    # 기본 세팅
    n = int(input())
    box = []
    for i in range(n):
        box.append(list(map(int,input().split())))
    arr = []
    for i in range(1,n):
        arr.append(i)
    N = len(arr)
    sel = [0] * N  # 결과들이 저장될 리스트
    check = [0] * N  # 해당 원소를 이미 사용했는지 안했는지에 대한 체크
    perm_list = []
    min_sum = 99999999
    perm(0)

    for i in range(0,len(perm_list)):
        count = 0
        for j in range(len(perm_list[i])-1):
            x = perm_list[i][j]
            y = perm_list[i][j+1]
            count +=box[x][y]
            if count >= min_sum:
                break

        if count < min_sum:
            min_sum = count
    print('#{} {}'.format(tc + 1, min_sum))

