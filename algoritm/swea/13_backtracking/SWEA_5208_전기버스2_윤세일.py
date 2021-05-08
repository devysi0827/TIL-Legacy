import sys
sys.stdin = open("1.txt","r")

def charge_plus(charge,batt, num):  #정류장넘버, 배터리, 교환횟수
    global min_change
    if charge == n:  # 마지막 정류장 이후로 도달할 수 있다면
        if num < min_change:  # 그 값에 초소 교환 횟수가 현재 최소보다 작다면
            min_change = num
            print(root)

    else:  # 아직 마지막 정류장이 아니라면
        batt = charge_list[charge]  #  현재 정류장만큼 배터리를 늘리고
        num += 1  #  교환횟수 +1
        root.append(charge)
        if num <= min_change: #  교환횟수가 최소 교환횟수를 넘지 않는다면
            for i in range(1,batt+1): #  배터리가 갈 수 있는 모든 곳을 방문한다.
                charge_plus(charge+i, batt-i, num)
                if charge+i >= n: #이미 넘었으면 반복문도 멈춘다.
                    break

tcs = int(input())
for tc in range(tcs):
    charge_list = list(map(int,input().split()))  # 정류장 리스트 받기
    n = charge_list[0]  # 정류장 수
    min_change = 99999999
    root = []
    charge_plus(1, 0, -1)  # 초기값: 1번 정류장(0번은 정류장 수), 배터리 = 0, 장착을 안해서 -1
    print("#{} {}".format(tc + 1, min_change))