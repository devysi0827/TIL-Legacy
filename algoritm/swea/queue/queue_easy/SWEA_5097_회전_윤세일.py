import sys
sys.stdin = open("sample_input.txt","r")

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
case_num = int(input()) #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n, m = map(int,input().split( ))
    queue = list(map(int,input().split( )))
    rear = -1
    front = -1
    check = False
    cnt = 0
    while cnt < m:
        temp = deque()
        enque(temp)
        cnt+=1

    print("#{} {}".format(case + 1, queue[0]))
