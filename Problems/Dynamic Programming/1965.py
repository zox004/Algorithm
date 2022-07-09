n = int(input())

dp = [0] * (1001)
boxes = list(map(int, input().split()))

for box in boxes:
    dp[box] = max(dp[:box]) + 1

print(max(dp))
