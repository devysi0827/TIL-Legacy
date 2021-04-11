from _collections import deque
import sys
sys.stdin = open("1.txt","r")

def bfs(s, e):
    visit[e] = 1
    node_q = [e]


    while node_q:
        curr = node_q.pop(0)
        for next in range(v + 1):
            if visit[next] == 0 and nodes[curr][next] == 1:
                node_q.append(next)
                visit[next] = 1
                dist[next] = dist[curr] + 1
            if next == s:
                return dist[next]

    return dist[next]

t = int(input())
for tc in range(t):
    v, e = map(int,input().split())

    nodes = [[0 for _ in range(v+1)] for _ in range(v+1)]

    dist = [0]*(v+1)
    visit = [0] * (v+1)
    for _ in range(e):
        n1, n2 = map(int,input().split())
        nodes[n1][n2] = 1
        nodes[n2][n1] = 1
    s,g = map(int,input().split())


    print('#{} {}'.format(tc+1,bfs(s,g)))

