import heapq

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        current, u = heapq.heappop(pq)
        if current > dist[u]:
            continue
        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    return dist

graph = {
    'A': [('B',1),('C',4)],
    'B': [('A',1),('C',2),('D',5)],
    'C': [('A',4),('B',2),('D',1)],
    'D': [('B',5),('C',1)]
}
res = dijkstra(graph,'A')
for v in res:
    print(v,":",res[v])
