import sys
from collections import deque

input = sys.stdin.readline

def bfs(board: list, row: int, col: int):
    visited = [[False]*col for _ in range(row)]
    coor = [[-1,0], [1,0], [0,-1], [0,1]]
    deq = deque([[0, 0]])
    visited[0][0] = True
    amount = 0
    
    while deq:
        y, x = deq.popleft()
            
        for dy, dx in coor:
            ny = dy + y
            nx = dx + x
            
            if 0<=ny<row and 0<=nx<col and not visited[ny][nx]:
                if board[ny][nx]==1:
                    board[ny][nx] = 0
                    amount += 1
                else:
                    deq.append((ny, nx))
                    
                visited[ny][nx] = True
    
    return amount, board
            
def solution():
    n, m = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(n)]
    time = 0
    
    while True:
        tmp, cheese = bfs(cheese, n, m)
        time += 1
        
        if tmp==0:
            break
        else:
            amount = tmp
    
    print(time-1, amount, sep="\n")            
        
if __name__=="__main__":
    solution()
