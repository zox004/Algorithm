from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
visit = []
lst = []
ans = 0
m, n, k = map(int, input().split())
board = [[1 for _ in range(n)] for _ in range(m)]
for i in range(k):
    x, y, dx, dy = map(int, input().split())
    for i in range(y, dy):
        for j in range(x, dx):
            board[i][j] = 0

def bfs(coord, board):
    a, b = coord
    # if board[a][b]==0:
    #     exit(0)
    global m, n
    cnt = 1
    move = [(-1,0),(1,0),(0,-1),(0,1)]
    dq.append(coord)
    visit.append(coord)
    while dq:
        p = dq.popleft()
        for i in move:
            row = p[0] + i[0]
            col = p[1] + i[1]
            if 0<=row<m and 0<=col<n and (row, col) not in visit and board[row][col]==1:
                dq.append((row,col))
                visit.append((row, col))
                board[row][col] = 0
                cnt += 1
    return cnt

for i in range(m):
    for j in range(n):
        if board[i][j]==1:
            lst.append(bfs((i,j),board))
            ans += 1

print(ans)
lst.sort()
print(*lst)
