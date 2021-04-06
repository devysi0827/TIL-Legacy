import sys
sys.stdin = open("1.txt","r")

testcases = int(input())

for tc in range(testcases):
    n, m, l = map(int, input().split( ))
    tree = [0]*(n+1)
    for i in range(m):
        index, num = map(int, input().split())
        tree[index] = num


    for i in range(n-m,0,-1):
        if i*2+1 <=n:
            tree[i] = tree[i*2] + tree[i*2+1]
        elif i*2+1 >n:
            tree[i] = tree[i * 2]
    print(tree)
    print('#{} {}'.format(tc + 1, tree[l], ))

