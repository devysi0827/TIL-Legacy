import sys
sys.stdin = open("1.txt","r")

def same_parent(list_1, list_2):
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                ans = list_1[i]
                return ans

T = int(input())

for tc in range(T):
    # 노드 수와 지정넘버 받기
    v,e,c1,c2 = map(int,input().split( ))
    # 간선정보받기
    edge = list(map(int, input().split()))
    #기본세팅
    left = [0] *(v+1)
    right = [0] * (v + 1)
    parent = [0] * (v + 1)

    #왼,오 노드 배열 만들기
    for i in range(int(len(edge)/2)):
        n1, n2 = edge[i*2], edge[i*2+1]
        if left[n1] == 0:
            left[n1] = n2
        else:
            right[n1] = n2
        parent[n2] = n1

    # 스택을 이용하여 모든 자손정보 구하기, 시작은 n(자손을 구하고자 하는 노드)
    stack = [c1]
    my_parent_c1 = []
    stack_2 = [c2]
    my_parent_c2 = []
    # 자손이 스택안에 있다면 반복한다
    while stack:
        temp = stack.pop()
        if parent[temp]:
            stack.append(parent[temp])
            my_parent_c1.append(parent[temp])

    while stack_2:
        temp = stack_2.pop()
        if parent[temp]:
            stack_2.append(parent[temp])
            my_parent_c2.append(parent[temp])

    if len(my_parent_c2)>= len(my_parent_c1):
        ans = same_parent(my_parent_c1,my_parent_c2)
    else:
        ans = same_parent(my_parent_c2, my_parent_c1)

    count = 0
    # 스택을 이용하여 모든 자손정보 구하기, 시작은 n(자손을 구하고자 하는 노드)
    stack = [ans]
    # 자손이 스택안에 있다면 반복한다
    while stack:
        temp = stack.pop()
        # 현재 자손에 왼쪽이 존재한다면 count를 올리고 stack에 왼쪽 자손을 추가한다.
        if left[temp]:
            count += 1
            stack.append(left[temp])
        # 현재 자손에 오른쪽이 존재한다면 count를 올리고 stack에 오른쪽 자손을 추가한다.
        if right[temp]:
            count += 1
            stack.append(right[temp])
    print('#{} {} {}'.format(tc + 1,ans,count+1))
