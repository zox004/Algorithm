import sys
input = sys.stdin.readline

k, n = map(int, input().split())
utp = []

for _ in range(k):
    utp.append(int(input()))


def binary_search(start, end, target, data):
    mid = (start+end) // 2
    if start>end:
        return mid
        
    cut_num = sum([utp//mid for utp in data])
    
    if cut_num<target:
        end = mid - 1
    elif cut_num>=target:
        start = mid + 1
    return binary_search(start, end, target, data)
        

print(binary_search(1, max(utp), n, utp))
