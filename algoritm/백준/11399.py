import sys
sys.stdin = open("1.txt","r")

n = int(input())
time_arr = list(map(int,input().split()))
sort_arr = sorted(time_arr)
ans = 0
for i in range(n):
    ans += (n-i)*sort_arr[i]
print(ans)