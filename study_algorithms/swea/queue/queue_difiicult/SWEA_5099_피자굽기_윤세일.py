import sys
sys.stdin = open("sample_input.txt","r")

#함수
def enque(a):
    global rear
    rear += 1
    queue.append(a)

def deque():
    if len(queue) == 0:
        return
    global front
    front += 1
    return queue.pop(0)


#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n, m = map(int,input().split( ))
    cheese = list(map(int,input().split( )))
    pizza_num = 0
    rear = -1
    front = -1
    queue = [0]*n
    num_que = [0]*n
    i =0

    while 1:
        temp = deque()//2
        num_temp = num_que.pop(0)

        if temp == 0 and pizza_num < m:
            enque(cheese[pizza_num])
            num_que.append(pizza_num+1)
            pizza_num += 1
        elif temp !=0:
            enque(temp)
            num_que.append(num_temp)

        print(queue)
        if len(queue) == 1:
            break

    print("#{} {}".format(case+1, num_que[0]))


