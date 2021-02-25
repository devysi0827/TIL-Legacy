import sys
sys.stdin = open("1.txt","r")

#함수
def max_index(i):
    maxi = numbers[i]
    index = i
    for j in range(i,n):
        if numbers[j] > maxi:
            maxi = numbers[j]
            index =j

    return index

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    numbers = list(map(int,input().split( )))

    ans = 0
    i=0

    while i<n:
        index = max_index(i)
        for j in range(i,index):
            benefit = numbers[index] - numbers[j]
            if benefit >0:
                ans+= benefit
        i = index+1

    print("#{} {}".format(case+1,ans))