n = int(input())
dp = [[-1000] * (n+1) for _ in range(2)]
sequence = list(map(int, input().split()))

for i in range(1, n+1):
    dp[0][i] = max(dp[0][i-1]+sequence[i-1], sequence[i-1])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+sequence[i-1])

print(max(max(dp[0]),max(dp[1])))
