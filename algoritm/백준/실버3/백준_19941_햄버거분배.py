import sys
sys.stdin = open("1.txt", "r")

n, m = list(map(int,input().split()))
strings = list(input())

ans = 0

for i in range(len(strings)):
    if strings[i] == 'P':
        for j in range(i-m,i+m+1):
            if j < 0 or j >= n:
                continue
            if strings[j] == 'H':
                strings[j] = 'X'
                ans += 1
                flag = 1
                break

print(ans)


