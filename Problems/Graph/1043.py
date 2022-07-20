from collections import deque

n, m = map(int, input().split())
true = list(map(int, input().split()))[1:]
cnt = 0
ex = 0
total = []
ccnt = 0

for i in range(m):
    party = deque(map(int, input().split()))
    length =party.popleft()
    total.append(list(party))    
    for j in party:
        if j in true:
            for k in party:
                true.append(k)
for k in range(m):
    for i in total:
        for j in i:
            if j in true:
                for q in i:
                    true.append(q)
true = set(true)

for i in total:
    for j in i:
        if j in true:
            ex = 0
            break
        else:
            ex = 1
    if ex==1:
        cnt += 1
        
print(cnt)
