import sys
sys.stdin = open("input.txt","r")

#함수
def find_hmon(box_ele): #회문판단

    for i in range(len(box_ele)):
        if box_ele[i] != box_ele[-i-1]:  #앞뒤가 똑같은지 판별한다
            return False

    return True  #회문이면 True

def list_join(list_1):  #리스트  -> 문자열 전환
    join_list=''
    for i in list_1:
        join_list +=i
    return join_list

def box_change(box):  #정사각형 박스 뒤집기
    change_box =[]
    n = len(box)
    for i in range(n):
        temp=[]
        for j in range(n):
            temp += [box[j][i]]
        change_box.append(temp)
    return change_box

def maximum(now, answer): # 두 값중 큰 값 반환
    if now >= answer:
        return now
    else:
        return answer

def box_moving(box,i):  #box i번째 열에 모든 회문에 대해서
    box_ele = box[i]  #box의 i번째
    box_len = len(box)  #박스길이
    my_len = len(box)  #문자길이
    answer = 0

    while 1: #일정 조건까지 계속 반복한다.
        for i in range(box_len - my_len + 1):  #박스-문자길이
            my_box = box_ele[i:i+my_len]  #내 박스는 i번째부터, i
            check = find_hmon(my_box)

            if check == True:
                hmon = list_join(my_box)
                hmon_leng = len(hmon)
                answer= maximum(answer, hmon_leng)

        my_len -=1
        if my_len < answer:
            break

    return answer


#본문<-------------------->
case_num = 10  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    trash = input()
    n = 100
    box = []
    for i in range(n):
        temp = list(input())
        box.append(temp)

    #본문2<-------------------------->
    answer = 0
    for i in range(len(box)):  #가로 순회
        i_max = box_moving(box, i)
        answer = maximum(answer,i_max)

    box = box_change(box)

    for i in range(len(box)):  #세로 순회
        i_max = box_moving(box, i)
        answer = maximum(answer, i_max)

    print("#{} {}".format(case + 1, answer))


