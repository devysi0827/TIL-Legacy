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

# 주어진 DATA 값
data = '01D06079861D79F99F'
# 값 데이터
data_binary = ''
for i in range(len(data)):
    data_binary += change_two(data[i])

ans = []
check = 0

#만약 7로 딱 나누어 떨어지지 않는다면 마지막에 한 작업을 더해준다.
if len(data_binary)%7 != 0:
    for i in range(int(len(data_binary)/7)+1):
        x = 1
        n = 0
        if check ==1:
            break
        for j in range(6,-1,-1):
            #마지막 단계에서는 마지막부터 각 이진수값(1,2,4....64)을 곱해서 한단계씩 천천히 더해간다.
            if i == int(len(data_binary)/7):
                for k in range(len(data_binary)-1,i*7-1,-1):
                    n += int(data_binary[k]) * x
                    x = 2*x
                check = 1
                break
            n += int(data_binary[i*7+j])*x
            x = 2*x
        ans.append(n)

#7로 나누어 떨어진다면, 연습문제 1에서 한 방법 그대로 편하게 한다.
else:
    for i in range(int(len(data_binary) / 7)):
        x = 64
        n = 0
        for j in range(7):
            n += int(data_binary[i * 7 + j]) * x
            x = int(x / 2)
        ans.append(n)
print(ans)
