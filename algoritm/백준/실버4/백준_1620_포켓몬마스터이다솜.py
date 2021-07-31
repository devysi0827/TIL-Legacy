import sys
sys.stdin = open("1.txt","r")
input = sys.stdin.readline

# def find_pock_name(pock_name):
#     global names
#     for j in range(n):
#         if pock_name == names[j]:
#             return j

n,m = list(map(int,input().split()))

names = []
name_dics ={}
for i in range(n):
    temp = input().strip()
    names.append(temp)
    name_dics[temp] = i+1


for i in range(m):
    q = input().strip()
    if q.isdigit() == True:
        print(names[int(q)-1])
    else:
        print(name_dics[q])
