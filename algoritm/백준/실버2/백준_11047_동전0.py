import sys
sys.stdin = open("1.txt","r")

n , k = map(int,input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
limit_num = -1
for i in range(n):
    if coins[i] > k:
        limit_num = i-1
        break
    if i == n-1:
        limit_num = n-1

ans = 0
for i in range(limit_num,-1,-1):
    ans += int(k // coins[i])
    k -= coins[i]*int(k // coins[i])
print(ans)