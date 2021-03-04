import sys
sys.stdin = open("sample_input (3).txt","r")
#
#함수
def do_gbb(first, second):  #가위비위보 인덱스를 받아서 승자를 반환
    temp = tournament[first] - tournament[second]
    if temp == -2 or temp == 2:
        temp = temp * -1

    if temp >= 0:
        return first
    else :
        return second

def do_tor(num_1, num_2 = -1):  # 이분할을 이용하여, 승자들끼리 토너먼트 시작
    if num_2 == -1 :
        return num_1
    if num_1 == num_2:
        return num_1
    elif abs(num_1-num_2) == 1 :
        return do_gbb(num_1, num_2)
    else:
        now = len(tournament[num_1:num_2])//2
        return do_gbb(do_tor(num_1,num_1+now), do_tor(num_1+now+1,num_2))

    # if len(input_tor) == 1:
    #     return input_tor[0]
    # elif len(input_tor) == 2:
    #     return do_gbb(input_tor[0], input_tor[1])
    # else:
    #     length = len(input_tor)
    #     forward = input_tor[0:length//2]
    #     backward = input_tor[length//2:]
    #     return do_gbb(do_tor(forward), do_tor(backward))


#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    tournament = list(map(int,input().split( )))

    win_num = do_tor(0,len(tournament)-1)
    print("#{} {}".format(case+1,win_num+1))