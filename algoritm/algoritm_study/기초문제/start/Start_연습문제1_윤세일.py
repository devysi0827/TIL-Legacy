num = '0000000111100000011000000111100110000110000111100111100111111001100111'
ans = []

# 7씩 끊어서 앞부터 각 항의 값(64,32,16, ...,1)과 이진법을 곱한 값의 합(실제 수)를 ans에 기록한다
for i in range(int(len(num)/7)):
    x = 64
    n = 0
    for j in range(7):
        n += int(num[i*7+j])*x
        x = int(x/2)
    ans.append(n)
print(ans)
