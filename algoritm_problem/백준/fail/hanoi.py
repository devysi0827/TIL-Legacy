n = 3 #int(input())

def top(stack):
    top_stack = stack[-1]
    return  top_stack

def move_block():
    global gijoon
    block_list = [first_stack,second_stack,third_stack]
    move_block_list = []
    check = 1

    for i in range(len(block_list)): #모든 리스트를 비지 않게 초기값0 추가
        if len(block_list[i]) == 0:
            block_list[i].append(0)

    for i in range(len(block_list)):  #맨 위만 모은 임시 무브-블록_리스트 설정
        move_block_list.append(top(block_list[i]))

    for i in range(len(move_block_list)): #0이 있나요?
        if move_block_list[i] == 0:
            check = 0  # 0이 있습니다
            arrive = 2

    if check == 0 :  #제일 큰 수 가 빈 곳으로 이동한다
        maximum = 0
        for i in range(len(block_list)):
            if move_block_list[i] > maximum:
                maximum = move_block_list[i]
                departure = i
                if departure ==2:
                    arrive = 0

        block = block_list[departure].pop()
        block_list[arrive].append(block)
        total_move.append([departure+1,arrive+1])
        for i in range(len(block_list)):  #0 디폴트 값 삭제
            if len(block_list[i]) >=1 and block_list[i][0] == 0:
                del block_list[i][0]

        if len(third_stack) == 1 and third_stack[0] == gijoon:
            third_stack.pop()
            gijoon -= 1

    else:  # 0이 없다면
        dummy =list(move_block_list)
        dummy.sort()

        for i in range(len(move_block_list)):

            if move_block_list[i] == dummy[0]:
                departure = i

            if move_block_list[i] == dummy[1]:
                arrive = i

        block = block_list[departure].pop()
        block_list[arrive].append(block)
        total_move.append([departure+1, arrive+1])


#초기 설정
first_stack = []
second_stack = []
third_stack = []
total_move = []
gijoon = n
for i in range(n,0,-1):
    first_stack.append(i)

while len(third_stack) <= gijoon:
    move_block()

print(total_move)
