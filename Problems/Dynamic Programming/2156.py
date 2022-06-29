n = int(input())
grapes = [0]
dp = [0] * (n+1)

for i in range(n):
    grapes.append(int(input()))
if n<3:
    print(sum(grapes))
    exit(0)

dp[1] = grapes[1]
dp[2] = grapes[1] + grapes[2]

for i in range(3,n+1):
    dp[i] = max(grapes[i]+grapes[i-1]+dp[i-3], dp[i-1], dp[i-2]+grapes[i])

print(dp[n])
