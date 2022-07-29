rr, cc = map(int, input().split())
row, col, d = map(int, input().split())
board = []
clear = 0
cnt = 0
move = [(-1,0), (1,0), (0,1), (0,-1)]
'''
4 4
2 2 0
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
'''
for i in range(rr):
    board.append(list(map(int, input().split())))

while True:
    if board[row][col]==0:
        board[row][col] = 2
        cnt += 1
    for m in move:
        r = m[0] + row
        c = m[1] + col
        if 0<=r<rr and 0<=c<cc:
            if d==0:
                if board[row][col-1]==0:
                    clear = 0
                    col -= 1
                    d = 3
                    break
                    # clean(row, col-1, 3)
                else:
                    if clear==4 and board[row+1][col]==1:
                        print(cnt)
                        exit()
                    elif clear==4 and board[row+1][col]==2:
                        clear = 0
                        row += 1
                        break
                        # clean(row+1, col, 0)
                    clear += 1
                    d = 3
                    break
                    # clean(row, col, 3)
            elif d==1:
                if board[row-1][col]==0:
                    clear = 0
                    row -= 1
                    d = 0
                    break
                    # clean(row-1, col, 0)
                else:
                    if clear==4 and board[row][col-1]==1:
                        print(cnt)
                        exit()
                    elif clear==4 and board[row][col-1]==2:
                        clear = 0
                        col -= 1
                        break
                        # clean(row, col-1, 0)
                    clear += 1
                    d = 0
                    break
                    # clean(row,col, 0)
            elif d==2:
                if board[row][col+1]==0:
                    clear = 0
                    col += 1
                    d = 1
                    break
                    # clean(row, col+1, 1)
                else:
                    if clear==4 and board[row-1][col]==1:
                        print(cnt)
                        exit()
                    elif clear==4 and board[row-1][col]==2:
                        clear = 0
                        row -= 1
                        break
                        # clean(row-1, col, 0)
                    clear += 1
                    d = 1
                    break
                    # clean(row,col, 1)
            elif d==3:
                if board[row+1][col]==0:
                    clear = 0
                    row += 1
                    d = 2
                    break
                    # clean(row+1, col, 2)
                else:
                    if clear==4 and board[row][col+1]==1:
                        print(cnt)
                        exit()
                    elif clear==4 and board[row][col+1]==2:
                        clear = 0
                        col += 1
                        break
                        # clean(row, col+1, 0)
                    clear += 1
                    d = 2
                    break
                    # clean(row,col, 2)

print(cnt)
