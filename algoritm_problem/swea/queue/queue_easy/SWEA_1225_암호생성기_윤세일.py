import sys
sys.stdin = open("input.txt","r")

#함수
def enque(a):
    global rear
    rear += 1
    queue.append(a)

def deque():
    global front
    front += 1
    return queue.pop(0)

#본문<-------------------->
case_num = 10  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    trash = input()
    queue = list(map(int,input().split( )))
    rear = -1
    front = -1
    check = False
    cnt = 0
    while check == False:
        temp = deque()
        cnt += 1
        if cnt == 6:
            cnt = 1

        temp -= cnt
        if temp <= 0:
            temp = 0
            enque(temp)
            break
        else:
            enque(temp)

    print(*queue)

