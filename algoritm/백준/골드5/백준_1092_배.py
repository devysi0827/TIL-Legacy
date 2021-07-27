import sys
sys.stdin = open("1.txt","r")

n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)

print(cranes)
print(boxes)

count = len(boxes)
if cranes[0] < boxes[0]:
    print(-1)
    exit()

total_count = 0

while len(boxes) > 0:
    for i in range(len(cranes)):
        for j in range(len(boxes)):
            print(cranes[i],boxes[j])
            if cranes[i] >= boxes[j]:
                del boxes[j]
                break
    total_count += 1

print(total_count)



