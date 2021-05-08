import sys
sys.stdin = open("input.txt","r")

for tc in range(10):
    testcase, n = map(int, input().split( ))
    box = list(map(int,input().split( )))
    node=[]
    maximum = -1
    check = 0
    for i in range(len(box)):
        if i%2 ==0:
            node.append([box[i],box[i+1]])
        if box[i] == 99:
            arrive = int((i-1)/2)
        if box[i] > maximum and box[i] != 99:
            maximum = box[i]

    check_list = [[0]* (maximum+2) for _ in range(maximum+2)]

    for i in range(len(node)):
        x = node[i][0]
        y = node[i][1]
        if y == 99:
            y = maximum+1
        check_list[x][y] = 1

    stack = [0]
    while len(stack) > 0:
        new_x = stack.pop()
        for i in range(maximum+2):
            if check_list[new_x][i] == 1:
                stack.append(i)
        if maximum+1 in stack:
            check = 1
            break

    print('#{} {}'.format(tc+1, check))



