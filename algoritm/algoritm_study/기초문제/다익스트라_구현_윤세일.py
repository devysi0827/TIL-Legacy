def dij(s,distances): #시작점, 인접행렬,거리행렬
    for i in range(len(nodes)):
        if nodes[i] == s:
            s = i
            break
    queue = []
    for i in range(len(edges[s])):
        if edges[s][i] != 0 and edges[s][i] != n :
            queue.append(nodes[i])
            if distances[s] == n:
                distances[s] = 0
            temp = distances[s]+ edges[s][i]
            if temp < distances[i]:
                distances[i] =temp

    for i in range(len(queue)):
        new_s = queue.pop(0)
        dij(new_s, distances)

nodes = ['a','b','c','d','e','f']
n = 99999999
edges = [
    [0,3,4,n,n,n],
    [n,0,n,5,n,n],
    [n,1,0,4,5,n],
    [n,n,n,0,3,4],
    [n,n,n,n,0,5],
    [n,n,n,n,n,0],
]
distances = [n]*len(nodes)

dij('a',distances)
print(distances)