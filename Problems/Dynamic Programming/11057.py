n = int(input())

dp = [1] * 10

for _ in range(1, n):
    for i in range(10):
        dp[i] = sum(dp[i:])

print(sum(dp)%10007)
