import sys
sys.stdin = open("3.txt","r")

case_num = int(input())
for case in range(case_num):
    n, m ,k = list(map(int,input().split( )))
    time = list(map(int,input().split( )))

    for i in range(len(time)):
        for j in range(i+1,len(time)):
            if time[i] > time[j]:
                time[i], time[j] = time[j], time[i]

    bbang = 0
    people = 0
    ans = 'Possible'
    for arrive_time in time:
        bbang = (arrive_time//m)*k
        people +=1
        bbang -= people
        if bbang < 0:
            ans = 'Impossible'
            break

    print("#{} {}".format(case+1,ans))


