from itertools import permutations

def solution(k, dungeons):
    count=0
    answer=0
    k2=k
    n= len(dungeons)
    lst=[i for i in permutations(range(n),n)]
    for ls in lst:
        for l in ls:
            if k2>=dungeons[l][0]:
                k2-=dungeons[l][1]
                count+=1
        answer=max(answer,count)
        count=0
        k2=k
    
    return answer