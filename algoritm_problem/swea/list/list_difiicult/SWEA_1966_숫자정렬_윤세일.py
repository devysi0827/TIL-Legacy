import sys
sys.stdin = open("sample_input (3).txt","r")
case_num = int(input())  #최초반복횟수

#본문
for case in range(case_num):
    n = int(input())
    n_list = list(map(int,input().split( )))

    for i in range(n):
        for j in range(n):
            if i != j and n_list[j] >= n_list[i]:
                n_list[j], n_list[i] = n_list[i], n_list[j]

    print("#{} ".format(case+1), end="")
    print(*n_list)