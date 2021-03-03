# 함수
def enque(a):
    global rear
    rear += 1
    queue.append(a)

def deque():
    global front
    front += 1
    return queue.pop(0)

# 본문
n = 20
first_n = n
queue = [(1,0)]
rear = -1
front = -1
new_people = 1
count = [0]*10  #편의상 10개만 정의한다
total_satang = 0

while n > 0:
    num, cnt = deque()
    last_people = num
    cnt += 1
    n -= cnt
    total_satang += cnt
    count[num-1] += cnt
    new_people += 1
    enque((num,cnt))
    enque((new_people,0))

    print("현재 큐에 있는 사람수: {}".format(len(queue)))
    print("인당 사탕수:")
    print(*count[:new_people])
    if total_satang <= first_n:
        print("현재까지 나눠준 사탕수: {}".format(total_satang))
    else:
        print("현재까지 나눠준 사탕수: {}".format(first_n))


print("마지막에 가져간 사람: {}".format(last_people))

