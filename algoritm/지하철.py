import sys, itertools
sys.stdin = open("1.txt","r")

repeat = int(input())
for repeat_num in range(repeat):
    # basic input
    n = int(input())
    subway_people = list(map(int,input().split()))

    # 조건4 서로 다른 4개의 지하철
    nums = []
    for i in range(n):
        nums.append(i)
    comb = list(itertools.combinations(nums,4))
    # print(comb)

    # 조건2,3 인접한 역은 도착과 출발이 불가능
    subway_c2_c3 = []
    for i in range(len(comb)):
        selctedStations = comb[i]
        for j in range(3):
            if selctedStations[j] +1 == selctedStations[j+1]:
                break
            if j==2:
                subway_c2_c3.append(list(selctedStations))

    # 마지막역 첫역 추가
    staions = []
    for i in range(len(subway_c2_c3)):
        selctedStations = subway_c2_c3[i]
        if selctedStations[0] == 0 and selctedStations[3] == n-1:
            pass
        else:
            staions.append(selctedStations)
    # print(subway_c2_c3)
    # print(staions)

    # 조건1 두 노선은 교차할 수 없음
    subway_c1 = []
    for i in range(len(staions)):
        selctedStations = staions[i]
        first = [selctedStations[0],selctedStations[1],selctedStations[2],selctedStations[3]]
        second = [selctedStations[0], selctedStations[3], selctedStations[1], selctedStations[2]]
        subway_c1.append(first)
        subway_c1.append(second)
    # print(subway_c1)
    # print(subway_people)

    max_tadang = -1
    for i in range(len(subway_c1)):
        selctedStations = subway_c1[i]
        alpa = (subway_people[selctedStations[0]]+subway_people[selctedStations[1]]) * (subway_people[selctedStations[0]]+subway_people[selctedStations[1]])
        beta = (subway_people[selctedStations[2]]+subway_people[selctedStations[3]]) * (subway_people[selctedStations[2]]+subway_people[selctedStations[3]])
        tadang = alpa + beta
        if tadang > max_tadang:
            max_tadang = tadang

    print("#{} {}".format(repeat_num+1,max_tadang))
