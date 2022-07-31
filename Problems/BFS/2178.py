from collections import defaultdict, deque

n, m = map(int, input().split())
way = []
dq = deque()

for i in range(n):
    way.append(list(input()))

way[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq.append((0, 0))

while dq:
    y, x = dq.popleft()
    for i in range(4):
        col = x + dx[i]
        row = y + dy[i]
        
        if 0<=col<m and 0<=row<n:
            if way[row][col]=='1':
                way[row][col] = way[y][x] + 1
                dq.append((row, col))

print(way[n-1][m-1])
