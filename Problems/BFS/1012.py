from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    coord = []
    board = []
    visit = []
    ans = 0
    m, n, k = map(int, input().split())

    for i in range(n):
        board.append(list(map(int, '0'*m)))

    for i in range(k):
        coord.append(list(map(int, input().split())))
    
    
    coord = deque(coord)
    while coord:
        x, y = coord.popleft()
        board[y][x] = 1
    dx = [1, -1, 0 ,0]
    dy = [0, 0, 1, -1]
    
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                board[i][j] = 0
                coord.append((i, j))
                while coord:
                    a, b = coord.popleft()
                    for k in range(4):
                        row = dy[k] + a
                        col = dx[k] + b

                        if 0<=row<n and 0<=col<m:
                            if board[row][col]==1:
                                board[row][col] = 0
                                coord.append((row, col))
                ans += 1
    print(ans)
