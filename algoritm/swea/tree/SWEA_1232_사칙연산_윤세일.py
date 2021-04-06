import sys
sys.stdin = open("1.txt","r")

testcases = 10

for tc in range(testcases):
    n = int(input())
    box =[[0]]

    for i in range(n):
        temp = list(input().split( ))
        box.append(temp)
    tree = [0]*(n+1)
    # print(box)
    #
    for i in range(n,0,-1):
        if box[i][1] == '+':
            tree[i] = tree[int(box[i][2])] + tree[int(box[i][3])]
        elif box[i][1] == '-':
            tree[i] = tree[int(box[i][2])] - tree[int(box[i][3])]
        elif box[i][1] == '*':
            tree[i] = tree[int(box[i][2])] * tree[int(box[i][3])]
        elif box[i][1] == '/':
            tree[i] = int(tree[int(box[i][2])] / tree[int(box[i][3])])
        else:
            tree[i] = int(box[i][1])

    print('#{} {}'.format(tc + 1, tree[1]))