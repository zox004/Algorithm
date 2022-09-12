def solution(n, apeach):
    max_diff = 0
    ryan = [0 for _ in range(11)]
    result = [0 for _ in range(11)]

    for subset in range(1, 1 << 10):
        ryan_score = 0
        apeach_score = 0
        cnt = 0

        for i in range(10):
            if subset & (1 << i):
                ryan_score += 10 - i
                ryan[i] = apeach[i] + 1
                cnt += ryan[i]
            else:
                ryan[i] = 0
                if apeach[i]:
                    apeach_score += 10 - i

        if cnt > n:
            continue

        ryan[10] = n - cnt

        if ryan_score-apeach_score==max_diff:
            if ryan[::-1]>result[::-1]:
                result = ryan[:]
        elif ryan_score-apeach_score>max_diff:
            max_diff = ryan_score - apeach_score
            result = ryan[:]
            
    if max_diff==0:
        return [-1]

    return result
