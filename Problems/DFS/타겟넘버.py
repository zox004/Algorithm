def dfs(result, iteration, target):
    global answer
    
    if iteration==max_length:
        if result==target:
            answer += 1
            return 
    else:
        dfs(result+number_list[iteration], iteration+1, target)
        dfs(result-number_list[iteration], iteration+1, target)

def solution(numbers, target):
    global answer, result, max_length, number_list
    number_list = numbers
    answer = 0
    result = 0
    max_length = len(numbers)

    dfs(0, 0, target)
    
    return answer
