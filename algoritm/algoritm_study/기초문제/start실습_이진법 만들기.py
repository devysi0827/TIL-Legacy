import sys
sys.stdin = open("1.txt","r")

#네자리, 이진법으로 바꾸는 함수
def change_two(n):
    quotient = []

    while 1:
        #만약 n이 1과 같거나 작아진다면
        if n<=1:
            # 마지막 1을 추가하고
            quotient.append(n)
            #모든 삽입이 역순이었으므로 반대로 읽어서 순서를 맞춰준다.
            quotient = quotient[::-1]
            #쉽게 합치기 위해서 문자열형태로 합쳐서 반환해 준다.
            ans = ''
            for i in range(len(quotient)):
                ans += str(quotient[i])
            return ans
        # n이 1보다 크다면 2로 나눈 나머지를 추가하고 n을 반으로 쪼갠다
        namage = n%2
        quotient.append(namage)
        n= n//2


T= int(input())
for tc in range(T):
    m, num = map(int, input().split( ))
    num = change_two(num)
    ans = 'on'
    if len(num) < m:
        ans = 'off'
    else:
        for i in range(len(num)-1,len(num)-m-1,-1):
            if num[i] != '1':
                ans = 'off'
                break
    print('#{} {}'.format(tc + 1, ans))