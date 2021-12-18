import collections
import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split()) # 정점, 간선 수 입력 받기
graph = collections.defaultdict(list) # 빈 그래프 생성

for _ in range(V):
    u, v, w = map(int, input().split())
    graph[u].append(v,w) # 그래프 생성

# 다익스트라 알고리즘
def dijkstra(graph, start):
    Q = [(0, start)] # 우선순위 큐생성 (거리, 정점)
    distance = collections.defaultdict(int) # 거리 정보를 담을 자료구조 생성

    while Q:
        dist, node = heapq.heappop(Q) # 힙 추출
        if node not in distance: # 방문한 노드가 아니면 거리 정보 저장
            distance[node] = dist
            for v, w in graph[node]: # 인점 노드 탐색
                update = dist + w # 거리 정보 갱신
                heapq.heappush(Q, (Q, (update, v))) # 우선 순위 큐에 삽입

    # 최단 경로 존재 여부 판별, distance 수가 전체 정점 수와 같은지 확인
    if len(distance) == V:
        return max(distance.values()) # 최단 거리 추출
    return -1 # 최단 거리가 없으면 -1 반환