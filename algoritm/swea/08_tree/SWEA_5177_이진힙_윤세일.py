import sys
sys.stdin = open("1.txt","r")

testcases = int(input())

for tc in range(testcases):
    n = int(input())
    box = list(map(int,input().split( )))
    tree = [0]

    for i in range(len(box)):
        tree.append(box[i])
        num = i+1
        while num > 1:
            pre_num = int(num/2)
            if tree[num] < tree[pre_num]:
                tree[pre_num], tree[num] = tree[num], tree[pre_num]
            else:
                break
            num = pre_num

    #
    # for i in range(1, n):
    #     if i*2+1 <= n:
    #         if box[i] > box[i*2] or box[i] > box[i*2+1]:
    #             if box[i*2] >= box[i*2+1]:
    #                 box[i*2+1], box[i] = box[i], box[i*2+1]
    #             else:
    #                 box[i*2], box[i] = box[i], box[i*2]
    #     elif i*2 <= n :
    #         if box[i] > box[i * 2]:
    #             box[i * 2], box[i] = box[i], box[i * 2]

    temp_n = n
    sum_tree = 0
    while 1:
        temp_n = int(temp_n/2)
        sum_tree += tree[temp_n]
        if temp_n == 1:
            break
    print('#{} {}'.format(tc + 1, sum_tree))

