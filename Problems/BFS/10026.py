from collections import deque
import copy
# import sys

# input = sys.stdin.readline

n = int(input())
board = []

for i in range(n):
    board.append(list(input()))

weak_board = copy.deepcopy(board)
noweak_board = copy.deepcopy(board)

def bfs_noweak(table):
    noweak_dq = deque()
    for i in range(n):
        for j in range(n):
            if table[i][j]==0 or table[i][j]==1:
                continue
            else:
                color = table[i][j]
                table[i][j] = 1
                noweak_dq.append((i,j))
                while noweak_dq:
                    p, q = noweak_dq.popleft()
                    move = [(-1,0), (1,0), (0,1), (0,-1)]
                    for m in move:
                        row = p + m[0]
                        col = q + m[1]
                        if 0<=row<n and 0<=col<n:
                            if color==table[row][col]:
                                noweak_dq.append((row, col))
                                table[row][col] = 0
                            # if (color=='R' or color=='G') and (table[row][col]=='R' or table[row][col]=='G'):
                            #     weak += 1


def bfs_weak(table):
    weak_dq = deque()
    for i in range(n):
        for j in range(n):
            if table[i][j]==0 or table[i][j]==1:
                continue
            else:
                color = table[i][j]
                table[i][j] = 1
                weak_dq.append((i,j))
                while weak_dq:
                    p, q = weak_dq.popleft()
                    move = [(-1,0), (1,0), (0,1), (0,-1)]
                    for m in move:
                        row = p + m[0]
                        col = q + m[1]
                        if 0<=row<n and 0<=col<n:
                            if (color=='R' or color=='G') and (table[row][col]=='R' or table[row][col]=='G') or color==table[row][col]:
                                weak_dq.append((row, col))
                                table[row][col] = 0
bfs_weak(weak_board)
bfs_noweak(noweak_board)

weak_sum = 0
noweak_sum = 0
for a in weak_board:
    weak_sum += sum(a)

for b in noweak_board:
    noweak_sum += sum(b)


print(noweak_sum, weak_sum)
