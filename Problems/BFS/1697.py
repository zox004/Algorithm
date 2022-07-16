from collections import deque

INF = 100001
n, k = map(int, input().split())
dq = deque()
dist = [0] * INF

def bfs(end):
    dq.append(n)
    while dq:
        p = dq.popleft()
        if p==end:
            print(dist[p])
            break
        for nx in (p-1, p+1, p*2):
            if 0<=nx<INF and not dist[nx]:
                dist[nx] = dist[p] + 1
                dq.append(nx)

bfs(k)
