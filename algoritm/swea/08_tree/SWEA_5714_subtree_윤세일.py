import sys
sys.stdin = open("1.txt","r")

testcases = int(input())

for tc in range(testcases):
    e, n = map(int, input().split( ))
    edge = list(map(int,input().split( )))
    stack = []
    count = 1
    stack.append(n)

    while len(stack) >0:
        num = stack.pop()
        for i in range(0,e*2,2):
            if edge[i] == num:
                stack.append(edge[i+1])
                count +=1

    print('#{} {}'.format(tc+1,count))
