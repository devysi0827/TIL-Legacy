import sys
sys.stdin = open("sample_input.txt","r")

#함수

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    cards = input()
    patterns = ['S','D','H','C']
    count_box = [13, 13, 13, 13]
    check_box = []
    ans =''

    #풀이
    for i in range(0,len(cards),3):
        if ans == 'ERROR':
            break
        for j in range(len(patterns)):
            if cards[i]  == patterns[j]:
                count_box[j] -= 1
                if cards[i:i+3] in check_box:
                    ans = 'ERROR'
                    break
                    check_box.append(cards[i:i+3])
                else:
                    check_box.append(cards[i:i + 3])

    if ans == 'ERROR':
        print("#{} {}".format(case+1,ans))
    else:
        print("#{} ".format(case+1), end='')
        print(*count_box)