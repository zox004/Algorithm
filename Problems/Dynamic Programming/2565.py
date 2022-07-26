n = int(input())
wire = []
dp = [1] * (n)

for _ in range(n):
    wire.append(tuple(map(int, input().split())))
wire.sort()

for i in range(n):
    for j in range(i):
        if wire[i][1]>wire[j][1]:
            dp[i] = max(dp[j]+1, dp[i])
 
print(n-max(dp))
