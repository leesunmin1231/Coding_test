import heapq

def solution(n, paths, gates, summits):
    INF = int(1e9)
    edges = [[] for _ in range(n+1)]
    summits = set(summits)
    for a, b, c in paths:
        edges[a].append([c, b])
        edges[b].append([c, a])
    
    distance = [INF] * (n+1)
    result = [INF, INF]
    q = []
    for gate in gates:
        heapq.heappush(q, [0, gate])
        distance[gate] = 0

    while q:
        cost, dest = heapq.heappop(q)
        if dest in summits:
            if cost < result[1]:
                result = [dest, cost]
            elif cost == result[1] and dest < result[0]:
                result = [dest, cost]
            continue
        if distance[dest] < cost:
            continue
        for next_cost, next_dest in edges[dest]:
            new_intensity = max(next_cost, cost)
            if new_intensity < distance[next_dest]:
                heapq.heappush(q, [new_intensity, next_dest])
                distance[next_dest] = new_intensity
    return result