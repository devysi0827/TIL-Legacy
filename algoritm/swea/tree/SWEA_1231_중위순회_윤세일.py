import sys
sys.stdin = open("1.txt","r")

def middleorder(n):
    if n> 0:
        middleorder(left[n])
        middle_order.append(n)
        middleorder(right[n])

testcases = 10
for testcase in range(testcases):
    # 기본 인풋
    n = int(input())

    box = []
    for i in range(n):
        box.append(list(input().split( )))

    edge = []
    for i in range(len(box)):
        if len(box[i]) == 4:
            edge.append(int(box[i][0]))
            edge.append(int(box[i][2]))
            edge.append(int(box[i][0]))
            edge.append(int(box[i][3]))

        elif len(box[i]) == 3:
            edge.append(int(box[i][0]))
            edge.append(int(box[i][2]))

    alpa_box = []
    for i in range(len(box)):
        alpa_box.append(box[i][1])

    v= max(edge)
    e = int(len(edge) / 2)
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    pa = [0]*(n+1)
    middle_order = []

    for i in range(e):
        n1, n2 = edge[i * 2], edge[i * 2 + 1]
        if left[n1] == 0:
            left[n1] = n2
        else:
            right[n1] = n2

        pa[n2] = n1

    root = 0
    for i in range(1, v + 1):
        if pa[i] == 0:
            root = i
            break

    ans = []
    middleorder(root)
    for i in middle_order:
        ans.append(alpa_box[i-1])

    print('#{}'.format(testcase+1), end=' ')
    for i in range(len(ans)):
        if i == len(ans)-1:
            print(ans[i])
        else:
            print(ans[i], end='')
