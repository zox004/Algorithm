from collections import defaultdict
import heapq, sys
INF = sys.maxsize

def dijkstra(n, gates, summits):
    global answer
    heap = []
    distances = [INF] * (n+1)

    for gate in gates:
        heapq.heappush(heap, (0, gate))
        distances[gate] = 0

    while heap:
        distance, node = heapq.heappop(heap)

        if node in summits or distance>distances[node]:
            continue
                
        for next_node, weight in graph[node]:
            intensity = max(weight, distance)
            if distances[next_node]>intensity:
                distances[next_node] = intensity
                heapq.heappush(heap, (intensity, next_node))
    
    summits = list(sorted(summits))
    for summit in summits:
        if distances[summit]<answer[1]:
            answer[0] = summit
            answer[1] = distances[summit]

def solution(n, paths, gates, summits):
    global answer, graph
    answer = [0, INF]
    graph = defaultdict(list)

    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))

    dijkstra(n, gates, set(summits))

    return answer
