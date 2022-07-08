n, m = map(int, input().split())

trees = list(map(int, input().split()))
M = max(trees)

def binary_search(start, end, target, trees):
    mid = (start+end) // 2
    if start>end:
        return mid

    rest = sum([tree-mid if tree-mid>0 else 0 for tree in trees])
    
    if rest==target:
        return mid
    elif rest>target:
        start = mid + 1
    else:
        end = mid - 1
    return binary_search(start, end, target, trees)

print(binary_search(0, M-1, m, trees))
