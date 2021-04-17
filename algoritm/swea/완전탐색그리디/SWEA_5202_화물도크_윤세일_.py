import sys, copy
sys.stdin = open("1.txt","r")

T = int(input())

for tc in range(T):
    # 기본 세팅
    n = int(input())
    box = [list(map(int,input().split())) for _ in range(n)]
    print(box)
    box.sort(key=lambda x: x[1])
    print(box)
    cnt = 0
    end = 0

    for i in range(n):
        if end <= box[i][0]:
            cnt += 1
            end = box[i][1]
    print("#{} {}".format(tc + 1, cnt))
