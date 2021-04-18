#data_binary
def change_two(n):
    # 알파벳을 받을 시 해당 숫자로 전환해준다.
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

data = '0269FAC9A0'
binary_data = ''
#데이터 이진수로 표시
for i in range(len(data)):
    binary_data += change_two(data[i])

# 데이터에서 끝에서 처음으로 1인 위치 찾기
for i in range(len(binary_data)-1,-1,-1):
    if binary_data[i] == '1':
        first_one = i
        break

# 암호들 나열하기 59~52, 51~44 등의 형식으로 패스워드 뽑아오기
password = []
for i in range(int(first_one/6)):
    temp =''
    for j in range(first_one-i*6,first_one-(i+1)*6,-1):
        temp += binary_data[j]
        password.append(temp[::-1])

password_list = ['001101','010011','111011','110001','100011','110111','001011','111101','011001','101111']

#해당 패스워드를 패스워드_리스트와 비교하여서 숫자로 치환하기
ans = []
for i in range(len(password)):
    for j in range(len(password_list)):
        if password[i] == password_list[j]:
            ans.append(j)
#역순으로 프린트하면 답이 나옴
print(ans[::-1])
