t, w = map(int, input().split())

dp = [0] * (t+1)
plum = [0]

for i in range(t):
    plum.append(int(input()))
print(plum)
for i in range(w+1):
    for j in range(1, t+1):
        if i%2==0:
            if plum[j]==1:
                dp[j] = max(dp[j]+1, dp[j-1]+1)
            elif plum[j]==2:
                dp[j] = max(dp[j], dp[j-1])
        elif i%2==1:
            if plum[j]==1:
                dp[j] = max(dp[j], dp[j-1])
            elif plum[j]==2:
                dp[j] = max(dp[j]+1, dp[j-1]+1)
    print(dp)
