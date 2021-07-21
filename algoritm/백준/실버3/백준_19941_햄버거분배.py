import sys
sys.stdin = open("1.txt", "r")

n, m = list(map(int,input().split()))
strings = list(input())
print(n,m)
print(strings)

ans = 0

for i in range(len(strings)):
    flag = 0
    if strings[i] == 'P':
        for j in range(i-1,i-m-1,-1):
            if j < 0:
                break
            if strings[j] == 'H':
                strings[j] = 'X'
                ans += 1
                flag = 1
                break
        if flag == 1:
            continue
        for j in range(i + 1, i + m +1):
            if j >= n:
                break
            if strings[j] == 'H':
                strings[j] = 'X'
                ans += 1
                continue
print(ans)


