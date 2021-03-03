def enque(a):
    global rear
    rear += 1
    q.append(a)

def deque():
    global front
    front += 1
    return q.pop(0)

front = -1
rear = -1
q = []

enque(1)
enque(2)
enque(3)

print(deque(), end= " ")
print(deque(), end= " ")
print(deque())

