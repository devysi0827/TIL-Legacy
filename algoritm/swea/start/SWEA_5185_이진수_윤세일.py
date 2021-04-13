import sys
sys.stdin = open("1.txt","r")

#네자리, 이진법으로 바꾸는 함수
def change_two(n):
    #알파벳을 받을 시 해당 숫자로 전환해준다.
    if n =='A':
        n=10
    elif n == 'B':
        n=11
    elif n == 'C':
        n=12
    elif n == 'D':
        n=13
    elif n == 'E':
        n=14
    elif n == 'F':
        n=15
    else:
        n= int(n)

    quotient = []

    while 1:
        #만약 n이 1과 같거나 작아진다면
        if n<=1:
            # 마지막 1을 추가하고
            quotient.append(n)
            # 만약에 네자리(0000)가 아닌 두, 세자리(10, 100)라면 0을 추가해서 자릿수를 맞추어 줄거야
            if len(quotient) < 4:
                for i in range(len(quotient),4):
                    quotient.append(0)
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

T = int(input())
for tc in range(T):
    n, data = map(str,input().split( ))

    data_binary = ''
    for i in range(len(data)):
        data_binary += change_two(data[i])

    print('#{} {}'.format(tc + 1, int(data_binary)))
