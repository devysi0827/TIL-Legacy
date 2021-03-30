import sys
sys.stdin = open("sample_input.txt","r")

#함수
def get_five_true(i, j, check):
    vector = [[0,1],[1,0],[1,1], [-1,1]]
    for _ in range(5):
        if box[i][j] == '.':
            return False
        i = i + vector[check][0]
        j = j + vector[check][1]
    return True


#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    box = []
    ans = 'NO'
    for i in range(n):
        box.append(list(input()))

    # 풀이
    check = 0
    for i in range(n):  #행 우선순회
        for j in range(n-4):
            temp_ans = get_five_true(i, j, check)
            if temp_ans == True:
                ans = 'YES'
                break

    if ans == 'YES':  #맞다면, 프린트 후 생략한다.
        print("#{} {}".format(case + 1, ans))
        continue

    check = 1
    for i in range(n-4):  #열 우선순회
        for j in range(n):
            temp_ans = get_five_true(i, j, check)
            if temp_ans == True:
                ans = 'YES'
                break

    if ans == 'YES':
        print("#{} {}".format(case + 1, ans))
        continue

    check = 2
    for i in range(n - 4):  # 대각선 왼쪽 위부터 순회
        for j in range(n-4):
            temp_ans = get_five_true(i, j, check)
            if temp_ans == True:
                ans = 'YES'
                break

    check = 3
    for i in range(n-1,3,-1):  # 대각선 오른쪽 위부터 순회
        for j in range(n-4):
            temp_ans = get_five_true(i, j, check)
            if temp_ans == True:
                ans = 'YES'
                break

    print("#{} {}".format(case+1,ans))


