import sys
sys.stdin = open("sample_input (3).txt","r")
case_num = int(input())  #최초반복횟수
#함수

def matrix_bug(box, i, j, m):
    answer = 0
    for repeat in range(i, i+m):
        for repeat2 in range(j, j+m):
            answer += box[repeat][repeat2]
    return answer


#본문
for case in range(case_num):
    n, m = list(map(int,input().split( )))
    box = []
    for i in range(n):
        temp =list(map(int,input().split( )))
        box.append(temp)

    max_del = 0  #죽인 파리 수

    for i in range(n-m+1):
        for j in range(n-m+1):
            del_bug = matrix_bug(box, i, j, m)

            if del_bug >max_del:
                max_del =del_bug

    print("#{} {}".format(case+1, max_del))

