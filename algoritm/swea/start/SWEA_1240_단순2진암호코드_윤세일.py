import sys
sys.stdin = open("1.txt","r")

#이차원 배열에서 뒤에서 가장 처음 나오는 1 찾기
def find_location(x):
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if box[i][j] ==x:
                return [i,j]

T= int(input())
for tc in range(T):
    n, m = map(int, input().split( ))
    box = []
    for i in range(n):
        temp = list(map(int, input()))
        box.append(temp)
    #함수 이용해서 역순에서 최초 1 찾기
    first_one = find_location(1)

    password = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    #이진수로 바꿔주기
    binary_list = []
    for i in range(int(first_one[1] / 7)):
        temp = ''
        for j in range(first_one[1] - i * 7, first_one[1] - (i + 1) * 7, -1):
            temp += str(box[first_one[0]][j])
        binary_list.append(temp[::-1])
    # print(binary_list)

    #패스워드와 비교하여 숫자로 바꿔주기
    num_list = []
    for i in range(len( binary_list)):
        for j in range(len(password)):
            if  binary_list[i] == password[j]:
                num_list.append(j)
    # print(num_list[::-1])

    # 바른 암호가 맞는 지 검증해서 check에 더함
    num_list = num_list[::-1]
    check = 0
    for i in range(len(num_list)):
        if i == len(num_list)-1:
            check += num_list[i]
        elif i %2 == 0:
            check +=num_list[i]*3
        else:
            check += num_list[i]

    #바른암호가 맞으면 합 출력 아니면 0 출력
    if check%10 == 0:
        print('#{} {}'.format(tc + 1, sum(num_list)))
    else:
        print('#{} {}'.format(tc + 1, 0))