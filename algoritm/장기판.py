import sys, copy
sys.stdin = open("4.txt","r")

def find_two():
    for i in range(n):
        for j in range(n):
            if zangipan[i][j] == 2:
                return [i,j]
    return [-1,-1]

def attack(position_i,position_j, before_list):
    dummy_zangipan = copy.deepcopy(zangipan)
    dummy_before_list = copy.deepcopy(before_list)

    for i in range(len(before_list)):
        dummy_zangipan[before_list[i][0]][before_list[i][1]] = 0
    dummy_before_list.append([position_i,position_j])
    moving_position = []

    # 위로 가자
    x = position_i
    y = position_j
    flag = 0
    while x >0:
        x = x-1
        if flag == 1:
            break
        if dummy_zangipan[x][y] == 1 and x !=0:
            while x>0:
                x = x-1
                moving_position.append([x,y])
                if dummy_zangipan[x][y] == 1:
                    flag = 1
                    break

    # 아래로 가자
    x = position_i
    y = position_j
    flag = 0
    while x < n-1:
        x = x + 1
        if flag == 1:
            break
        if dummy_zangipan[x][y] == 1 and x != n-1:
            while x < n-1:
                x = x + 1
                moving_position.append([x, y])
                if dummy_zangipan[x][y] == 1:
                    flag = 1
                    break

    # 왼쪽으로 가자
    x = position_i
    y = position_j
    flag = 0
    while y > 0:
        y = y - 1
        if flag == 1:
            break
        if dummy_zangipan[x][y] == 1 and y != 0:
            while y > 0:
                y = y - 1
                moving_position.append([x, y])
                if dummy_zangipan[x][y] == 1:
                    flag = 1
                    break

    # 오른쪽으로 가자
    x = position_i
    y = position_j
    flag = 0
    while y < n - 1:
        y = y + 1
        if flag == 1:
            break
        if dummy_zangipan[x][y] == 1 and y != n - 1:
            while y < n - 1:
                y = y + 1
                moving_position.append([x, y])
                if dummy_zangipan[x][y] == 1:
                    flag = 1
                    break

    return_list = []
    return_list.append(dummy_before_list)
    return_list.append(moving_position)

    return return_list


repeat = int(input())
for repeat_num in range(repeat):
    # basic input
    n = int(input())
    zangipan = []
    for i in range(n):
        zangipan.append(list(map(int,input().split())))
    # print(zangipan)
    catched_list = []
    positon = find_two()
    # 첫 공격
    first_attack = attack(positon[0],positon[1],[])
    first_before_list = first_attack[0]
    first_move_list = first_attack[1]
    # print(first_move_list)
    # 첫 공격 위치 통합
    for i in range(len(first_move_list)):
        if zangipan[first_move_list[i][0]][first_move_list[i][1]] == 1:
            if first_move_list[i] not in catched_list:
                catched_list.append(first_move_list[i])
    # print(catched_list)

    # 두번째 공격
    second_attacks = []
    for i in range(len(first_move_list)):
        x = first_move_list[i][0]
        y = first_move_list[i][1]
        second_attack = attack(x, y, first_before_list)
        second_attacks.append(second_attack)
    # print(second_attacks)
    # 두번째 공격 통합
    for i in range(len(second_attacks)):
        now_list = second_attacks[i][1]
        for j in range(len(now_list)):
            now_position_list = now_list[j]
            if zangipan[now_position_list[0]][now_position_list[1]] == 1:
                if now_position_list not in catched_list:
                    catched_list.append(now_position_list)

    # print(catched_list)

    # 세번째 공격
    third_attacks = []
    for i in range(len(second_attacks)):
        now_attack = second_attacks[i] # [[[3, 2], [1, 2]], [[3, 2], [4, 2], [1, 0]]
        second_before_list = now_attack[0]
        second_move_list = now_attack[1]
        for i in range(len(second_move_list)):
            x = second_move_list[i][0]
            y = second_move_list[i][1]
            third_attack = attack(x, y, second_before_list)
            third_attacks.append(third_attack)
    # print(third_attacks)
    # 세번째 공격 통합
    for i in range(len(third_attacks)):
        now_list = third_attacks[i][1]
        for j in range(len(now_list)):
            now_position_list = now_list[j]
            if zangipan[now_position_list[0]][now_position_list[1]] == 1:
                if now_position_list not in catched_list:
                    catched_list.append(now_position_list)

    # print(catched_list)
    catched_zangi = len(catched_list)
    print("#{} {}".format(repeat_num + 1, catched_zangi))
