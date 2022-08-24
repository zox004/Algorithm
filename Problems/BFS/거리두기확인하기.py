from collections import deque

def bfs(place):
    move = [[-1,0], [1,0], [0,-1], [0,1]]

    for i in range(5):
        for j in range(5):
            distance = [[0]*5 for _ in range(5)]

            if place[i][j]=="P":
                visited = []
                dq = deque()
                dq.append([i,j])

                while dq:
                    y, x = dq.popleft()

                    for dy, dx in move:
                        row = dy + y
                        col = dx + x
                        if [row, col] in visited:
                            continue
                        else:
                            if 0<=row<5 and 0<=col<5:
                                if place[row][col]=="O" or place[row][col]=="P":
                                    dq.append([row, col])
                                    visited.append([y, x])
                                    distance[row][col]= distance[y][x] + 1

                                if place[row][col]=="P" and distance[row][col]<=2:
                                    return 0
    else:
        return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place))
    
    return answer
