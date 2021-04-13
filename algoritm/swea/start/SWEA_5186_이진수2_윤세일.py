import sys
sys.stdin = open("1.txt","r")

T = int(input())
for tc in range(T):
    n = float(input())
    ans_list = []
    check = 0
    x = 0.5
    while n > 0:
        if n >= x:
            n = n-x
            ans_list.append(1)
            x= x/2
        else:
            ans_list.append(0)
            x= x/2
        if len(ans_list) >12:
            check = 1
            ans = 'overflow'
            break
    if check == 1:
        print('#{} {}'.format(tc + 1, ans))
    else:
        ans = ''
        for i in range(len(ans_list)):
            ans += str(ans_list[i])
        print('#{} {}'.format(tc + 1, ans))
