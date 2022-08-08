import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    ans = 1
    lst = [0 for _ in range(n)]
    
    for i in range(n):
        a, b = map(int, input().split())
        lst[a-1] = b
        
    m = lst[0]
    for i in lst:
        if m>i:
            ans += 1
            m = i
    print(ans)
