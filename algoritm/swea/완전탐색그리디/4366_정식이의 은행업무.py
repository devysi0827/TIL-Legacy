import sys
sys.stdin = open("1.txt","r")

def two_point(list_two):
    n = len(list_two)
    ans = 0
    for i in range(len(list_two)):
        if list_two[i] == '1':
            ans += 2**(n-i-1)
    return ans

def find_same(list_1, list_2):
    for i in range(len(list_1)):
            if list_1[i] in list_2:
                return list_1[i]

def three_point(list_three):
    n = len(list_three)
    ans = 0
    for i in range(len(list_three)):
        if list_three[i] == '1':
            ans += 3**(n-i-1)
        elif list_three[i] == '2':
            ans += 3**(n-i-1)*2
    return ans

T = int(input())

for tc in range(T):
    # 기본 세팅
    num_two = list(input())
    num_three = list(input())

    num_two_to_ten = []
    for i in range(len(num_two)):
        temp = list(num_two)
        if num_two[i] == '1':
            temp[i] = '0'
        else:
            temp[i] = '1'
        num_two_to_ten.append(two_point(temp))

    num_three_to_ten = []
    for i in range(len(num_three)):
        temp = list(num_three)
        temp_n = num_three[i]
        for j in range(3):
            # if i ==0 and j==0:
            #     continue
            if temp_n == 'j':
                continue
            temp[i] = str(j)
            num_three_to_ten.append(three_point(temp))
    print(num_three_to_ten)
    print(num_two_to_ten)
    n2 = sorted(num_two_to_ten)
    n3 = sorted(num_three_to_ten)

    ans = find_same(n2,n3)

    print('#{} {}'.format(tc + 1, ans))



