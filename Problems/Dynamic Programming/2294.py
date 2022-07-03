n, k = map(int, input().split())
INF = 1000000

coin = [int(input()) for _ in range(n)]
dp = [INF for i in range(k+1)]

dp[0] = 0

for i in coin:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i]+1)
if dp[k]==INF:
    print(-1)
else:
    print(dp[k])
