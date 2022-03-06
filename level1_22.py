def solution(arr):
    answer=[10]
    for i in arr:
        if i==answer[-1]:
            continue
        answer.append(i)
    del answer[0]
    
    return answer