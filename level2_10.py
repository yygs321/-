def solution(citations):
    result=[0]*(max(citations)+1)
    answer=0
    sum=0
    for c in citations:
        result[c]+=1
    for idx,r in enumerate(result[::-1]):
        sum+=r
        if sum>=len(result)-1-idx:
            answer=max(answer,len(result)-1-idx)
            
    return answer