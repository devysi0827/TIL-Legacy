#  입력
import sys
sys.stdin = open("2.txt","r")
case_num = int(input())


for case in range(case_num):
    # 기본 설정
    num = int(input())
    list_num = []
    for repeat in range(num):
        new_list = []# 달팽이가 들어갈 리스트
        for repeat2 in range(num):
            new_list.append(0)
        list_num.append(new_list)

    numbers = []
    for i in range(num**2):
        numbers.append(i+1)  # 1~16까지 리스트

   # 시작
    count = 0
    j = 0
    check_num = 0
    for index in range(2*num -1):
         i = index //2
         #  1234
         if index%2 ==0:
             if index % 4 ==0:
                 for j in range(i,num):
                    list_num[i][j] = numbers[check_num]
                    check_num +=1

             else:
                 for j in range(i,num):
                    list_num[4-i-1][num-j-1] = numbers[check_num]
                    check_num +=1

         # 567
         if index%2 ==1:
             if index % 4 ==1:
                 for j in range(i+1, num):
                     list_num[j][num-i-1] = numbers[check_num]
                     check_num += 1

             if index % 4 == 3:
                 for j in range(num, i+2, -1):
                     list_num[i-1][num-j+1] = numbers[check_num]
                     check_num += 1



    print(list_num)