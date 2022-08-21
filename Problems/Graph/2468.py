from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
board1 = []
board2 = []
ans = []
dq = deque()

for i in range(n):
    tmp = list(map(int, input().split()))
    board1.append(tmp)
    tmp2 = [i for i in tmp]
    board2.append(tmp2)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for height in range(101):
    if 0 in ans:
        break
    for y in range(n):
        for x in range(n):
            if board2[y][x]<=height:
                board1[y][x] = 0
            else:
                board1[y][x] = 1

    cnt = 0
    for y in range(n):
        for x in range(n):
            if board1[y][x]==1:
                board1[y][x] = 0
                cnt += 1
                dq.append((y, x))
                while dq:
                    b, a = dq.popleft()
                    for k in range(4):
                        row = dy[k] + b
                        col = dx[k] + a
                        if 0<=row<n and 0<=col<n:
                            if board1[row][col]==1:
                                board1[row][col] = 0
                                dq.append((row, col))      
    ans.append(cnt)
print(max(ans))
