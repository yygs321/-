def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i==j:
                continue
            answer.append(numbers[i]+numbers[j])
    answer=sorted(set(answer)) #tuple은 중복 가능, set은 중복 불가
    
    return answer