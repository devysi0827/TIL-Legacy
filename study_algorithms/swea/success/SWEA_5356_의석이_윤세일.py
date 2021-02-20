import sys
sys.stdin = open("sample_input.txt","r")

#함수
def max_leng(box):  #최대 행길이
    max = 0
    for i in box:
        if max <len(i):
            max =len(i)

    return max

def get_same_leng(box,max):  #박스 길이 맞추기 함수
    for box_i in box:
        while len(box_i) < max:
            box_i.append('')

    return box



#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    box = []
    for i in range (5):
        temp = list(input())
        box.append(temp)

    # 박스 길이 맞추기
    max_len = max_leng(box)
    get_same_leng(box, max_len)

    answer = ''
    for i in range(max_len):
        for j in range(5):
            if box[j][i]:
                answer += box[j][i]

    print('#{} {}'.format(case+1, answer))

