def solution(d, budget):
    result=0
    while d:
        m=min(d)
        if budget<m:
            break
        d.remove(m)
        budget-=m
        result+=1
        
    return result