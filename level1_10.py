def solution(n):
    num = list(map(int,str(n)))
    answer=[]
    for i in range(len(num)-1,-1,-1):
        answer.append(num[i])
    return answer