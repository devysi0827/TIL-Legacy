import sys
sys.stdin = open("sample_input.txt","r")

#함수

# event =['11','2','3']
# new_event = []
#a = soonyeol(2)

def soonyeol(n):

    if n ==0:
        return event
    else:
        for i in soonyeol(n-1):
            for j in event:
                new_event.append([i] + [j])

        return new_event



# #본문<-------------------->
# case_num = int(input())  #최초반복횟수
# for case in range(case_num):
#     # 기본 인풋을 이용한 박스형성
#     n = int(input())
#     n = n//10
#     event =['11','2','3']
#     var = ['1']
#
#     if n%2 == 0:
#         ans = 3**n//2
#     else:
#

    # print("#{} {}".format(case+1,ans))

event =['11','2','3']
var = ['1']
new_event = []

# for i in event:
#     for j in event:
#         for k in event:
#             lis +=[[i,j,k]]

a = soonyeol(2)
print(a)


