def solution(clothes):
    answer = 1
    dic={}
    
    for c in clothes:
        if c[1] in dic.keys():
            dic[c[1]]+=1
        else:            
            dic[c[1]]=1

    dic_values=dic.values()
    for d in dic_values:
        answer*=(d+1)
    answer-=1
    return answer
