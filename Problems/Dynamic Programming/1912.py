n = int(input())
dp = [-1000] * (n+1)
sequence = list(map(int, input().split()))

for i in range(1, n+1):
    dp[i] = max(dp[i-1]+sequence[i-1], sequence[i-1])

print(max(dp))
