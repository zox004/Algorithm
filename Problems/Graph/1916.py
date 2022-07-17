import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if dist>distance[node]:
            continue
        else:
            for next in graph[node]:
                cost = distance[node] + next[0]
                if cost<distance[next[1]]:
                    distance[next[1]] = cost
                    heapq.heappush(q, (cost, next[1]))

n = int(input())
m = int(input())
distance = [int(1e8)] * (n+1)
graph = defaultdict(list)

for i in range(m):
    start, end, w = map(int, input().split())
    graph[start].append((w, end))
    
a, z = map(int, input().split())
dijkstra(a)
print(distance[z])
