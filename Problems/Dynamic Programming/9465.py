t = int(input())

for _ in range(t):
    ans = 0
    n = int(input())
    lst = []
    for i in range(2):
        lst.append(list(map(int, input().split())))

    if n<3:
        if n==1:
            ans = max(lst[0][n-1], lst[1][n-1])
        else:
            lst[0][1] += lst[1][0]
            lst[1][1] += lst[0][0]
    else:
        lst[0][1] += lst[1][0]
        lst[1][1] += lst[0][0]
        for i in range(2, n):
            lst[0][i] += max(lst[0][i-2], lst[1][i-2], lst[1][i-1])
            lst[1][i] += max(lst[1][i-2], lst[0][i-2], lst[0][i-1])
    ans = max(lst[0][n-1], lst[1][n-1])
    print(ans)
