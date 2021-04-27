import sys
sys.stdin = open("1.txt","r")

def Prim():
    ## 초기값들 세팅
    # 가중치 박스 => 간선 사이 최소 가중치들이 기록될 예정임 => 따라서 일단 굉장히 큰 박스
    dist = [987654321] * (V+1)
    #방문 여부 체크
    visited = [False]* (V+1)
    # 시작 정점의 키 값을 0으로 초기화!!!!!! // 0,1,2 ... v까지 아무거나 상관없음!
    dist[0] = 0

    ##
    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        ## 방문한 노드들과 연결된 간선들 중 가장 작은 간선 찾기
        for i in range(V+1):
            # 방문하지 않은 노드중, 해당 노드의 값이 최소값보다 작다면, 해당값과 해당인덱스를 기록한다.
            # dist[i] < min_value가 되려면, 방문한 노드들의 인접 간선들만 가능함
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]

        # 현재 방문 가능한 가장 최소값을 방문 체크한다.
        # 방문한 노드가 이제 기준이 된다.
        visited[min_idx] = True

        ##
        # 방문 노드의 인접 노드들(연결된 노드)에 대해서,
        # 방문한지 않았고(중복 계산 방지)
        # 현재 기록된 가중치(초기값:infinity, 갱신되었다면 갱신값)보다
        # 작은 가중치값(adj(인접리스트)에 기록도니 값)이 있다면 그 값으로 변경
        # 이 과정을 모든 노드에 대해서 반복하면 최소값 n-1개를 가진 dist가 완성된다.
        for i in range(V+1):
            if not visited[i] and adj[min_idx][i] < dist[i]:
                dist[i] = adj[min_idx][i]
    # 구하는 것은 최소신장이므로 이 값을 모두 합친걸 반환한다,
    return sum(dist)


for tc in range(1, int(input())+1):
    #노드 개수/ 간선의 개수
    V, E = map(int,input().split())
    # 인접리스트 만들기 기본값은 = infi(매우 큰수)
    adj = [[987654321] * (V+1) for _ in range(V+1)]

    for i in range(E):
        ## 인풋 받기
        # 출발노드/ 도착노드/ 가중치
        st, ed, w = map(int, input().split())
        # 인접리스트에 가중치 표기
        adj[st][ed] = adj[ed][st] = w

    print("#{} {}".format(tc, Prim()))