import heapq

edges = [
    (1, 2, 1),
    (1, 11, 1),
    (2, 3, 1),
    (2, 11, 1),
    (2, 21, 1),
    (3, 4, 1),
    (3, 8, 2),
    (4, 5, 1),
    (5, 7, 1),
    (5, 22, 1),
    (5, 6, 2),
    (6, 7, 1),
    (7, 8, 1),
    (8, 9, 1),
    (9, 10, 1),
    (9, 19, 1),
    (10, 11, 1),
    (10, 18, 1),
    (11, 12, 2),
    (11, 17, 1),
    (12, 13, 2),
    (13, 14, 2),
    (13, 21, 1),
    (14, 15, 1),
    (14, 16, 1),
    (14, 20, 1),
    (16, 17, 2),
    (17, 18, 1),
    (18, 19, 2),
    (20, 21, 2),
    (20, 22, 1),
    (21, 22, 2),
]

n = 22
graph = {i: [] for i in range(1, n + 1)}

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}
    
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))
    
    return dist, parent
