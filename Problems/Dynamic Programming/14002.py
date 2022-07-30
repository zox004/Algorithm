n = int(input())
sequence = [1001, *map(int, input().split())]
dp = [1] * (n+1)
dp[0] = 0
answer = []

for i in range(1, n+1):
    for j in range(1, i+1):
        if sequence[j-1]<sequence[i]:
            dp[i] = max(dp[i], dp[j-1]+1)
cnt = max(dp)
print(max(dp))

for i in range(n, 0, -1):
    if cnt == dp[i]:
        cnt -=1
        answer.append(sequence[i])
print(*answer[::-1])
