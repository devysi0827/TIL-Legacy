import sys

sys.stdin = open("2.txt","r")

def mnmultiply(n_list, m_list, n, repeat):  #n이 작을때 기준 작성
    value = 0
    for index in range(n):
        value += n_list[index] * m_list[index + repeat]
    return value

#<--------------------------입출력 ------------------>
test_case = int(input())  #최초 인풋 총 반복 수
for case in range(test_case):

    n, m = list(map(int,input().split( )))  #넘버 받기
    n_list=list(map(int,input().split( )))  #n리스트 받기
    m_list=list(map(int,input().split( )))  #m리스트 받기

    if n<= m:
        max_value = mnmultiply(n_list, m_list, n, 0)
        for repeat in range(m-n+1):
            value = mnmultiply(n_list, m_list, n, repeat)
            if value > max_value:
                max_value =value
    else:
        max_value = mnmultiply(m_list, n_list, m, 0)
        for repeat in range(n - m + 1):
            value = mnmultiply(m_list, n_list, m, repeat)
            if value > max_value:
                max_value = value
    print("#{} {}".format(case+1,max_value))
#<------------------------ 기본 항 설정 --------------------------------------->