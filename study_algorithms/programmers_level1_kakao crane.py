def find_non_zero(list_1,num):
    list_2 = []
    for i in range(len(list_1[num-1])):
        if list_1[num-1][i] !=0 :
            list_2.append(list_1[num-1][i])
            list_2.append(i)
            return list_2
    return [0,0] #없을 경우 더미값 반환


def change_zero(list_1,num,i):
    list_1[num-1][i]=0


def solution(board, moves):
    answer = 0  # 사라진 개수
    basket = [0]  # 담을 공간
    n = len(board)  # 길이

    # 이차원 배열 만들기
    new_board = []
    for i in range(n):
        temp_list=[]
        for j in range(n):
            temp_list.append(0)
        new_board.append(temp_list)

    # 바꾸기
    for i in range(n):
        for j in range(n):
            new_board[i][j] =board[j][i]

    # basket 만들기
    for move in moves:
        charactor = find_non_zero(new_board, move)
        if basket[-1] == charactor[0]  and charactor[0]!=0:
            del basket[-1]
            answer+=2
        else:
            basket.append(charactor[0])
        change_zero(new_board, move, charactor[1])

    # 모든 0 제거
    check = True
    while check == True:
        if 0 in basket:
            basket.remove(0)
        if 0 not in basket:
            check =False

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))


