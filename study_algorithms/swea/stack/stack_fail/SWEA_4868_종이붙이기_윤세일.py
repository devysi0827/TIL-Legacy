import sys
sys.stdin = open("1.txt","r")

#함수
def get_paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return get_paper(n-1)+2*(get_paper(n-2))

#본문
case_num = int(input())  # 최초반복횟수
for case in range(case_num):
    n=int(input())
    ans = get_paper(int((n/10)))
    print('#{} {}'.format(case+1, ans))

