def solution(N, stages):
    fail={}
    l=len(stages)
    for i in range(1,N+1):
        #맨마지막 스테이지까지 도달한 사람이 없을 경우
        if l<=0:
            fail[i]=0
            continue        
        fail[i]=stages.count(i)/l
        l-=stages.count(i)

    #딕셔너리 value값 기준으로 내림차순 정렬
    answer= [j[0] for j in (sorted(fail.items(), reverse=True,key=lambda item: item[1]))]
    
    return answer