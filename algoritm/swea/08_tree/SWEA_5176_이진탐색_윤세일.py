import sys
sys.stdin = open("1.txt","r")

testcases = int(input())

def middleorder(n):
    global num
    if n> 0:
        middleorder(left[n])
        num +=1
        middle_order[n] = num
        middleorder(right[n])

for tc in range(testcases):
    n = int(input())
    root = 1
    edge = []
    num = 0

    for i in range(1,n+1):
        if i*2 <=n:
            edge.append(i)
            edge.append((i*2))
            if i*2+1 <= n:
                edge.append(i)
                edge.append((i*2+1))

    v = max(edge)
    e = int(len(edge) / 2)
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    pa = [0] * (n + 1)
    middle_order = []
    for i in range(n+1):
        middle_order.append(i)


    for i in range(e):
        n1, n2 = edge[i * 2], edge[i * 2 + 1]
        if left[n1] == 0:
            left[n1] = n2
        else:
            right[n1] = n2

    root =1
    middleorder(root)
    # print(middle_order)


    print('#{} {} {}'.format(tc+1, middle_order[1], middle_order[int(n/2)]))
