import sys
sys.stdin = open("1.txt","r")

#함수
def find_hmon(box_ele,m): #회문판단
    if len(box_ele) != m:  # 길이가 m이 아니라면 무시한다 조건 추가
        return False

    if len(set(box_ele)) == 1:  #단일문자라면, 회문으로 취급하지 않는다
        return False

    for i in range(len(box_ele)):
        if box_ele[i] != box_ele[-i-1]:  #앞뒤가 똑같은지 판별한다
            return False

    return True  #모든 조건을 통과하면 True

def list_join(list_1):  #리스트  -> 문자열 변환
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

def switch_slicing(box_ele,n):  #선택형 슬라이싱함수

    if n == 1:
        box_ele = box_ele[1:]
    if n == -1:
        box_ele = box_ele[:-1]

    return box_ele

def box_moving(box,i,m):  #box i번째 열에 화문이 있나요?
    check = False  #디폴트 설정
    box_ele = box[i]  #box의 i번째

    while check == False:
        check = find_hmon(box_ele, m)

        if check == False:
            box_ele = switch_slicing(box_ele,1)  #1이면 [1:] -1이면 [0:-1]

        else:
            answer = list_join(box_ele) #문자열화
            return answer

        if len(box_ele) == 1:
            break

    box_ele = box[i]
    while check == False:
        check = find_hmon(box_ele, m)

        if check == False:
            box_ele = switch_slicing(box_ele, -1)  # 1이면 [1:] -1이면 [0:-1]

        else:
            answer = list_join(box_ele)  # 문자열화
            return answer

        if len(box_ele) == 1:
            return None


#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n, m  =map(int,input().split( ))
    box = []
    for i in range(n):
        temp= list(input())
        box.append(temp)

    #본문2<-------------------------->
    for i in range(len(box)):  #가로 순회
        answer = box_moving(box, i, m)
        if answer:
            print("#{} {}".format(case + 1, answer))
            break

    if answer:  #가로에서 찾았다면 수행하지 않는다
        continue

    box = box_change(box)

    for i in range(len(box)):  #세로 순회
        answer = box_moving(box, i, m)
        if answer:
            print("#{} {}".format(case + 1, answer))
            break

