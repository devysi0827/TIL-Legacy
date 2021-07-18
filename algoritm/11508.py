import sys
sys.stdin = open("1.txt","r")

n = int(input())
box = []
for i in range(n):
    box.append(int(input()))
box = sorted(box)

cnt =0
ans = 0
for i in range(len(box)-1,-1,-1):
    cnt +=1
    if cnt %3 == 0:
        pass
    else:
        ans += box[i]
print(ans)

