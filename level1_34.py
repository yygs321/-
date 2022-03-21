def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    have=[i for i in range(1,n+1) if i not in lost]
    for l in lost:
        if l in reserve: #여벌 옷 가진 학생이 잃어버린 경우 여벌 옷 없는 것으로 간주
            have.append(l)
            reserve.remove(l) 
            lost.remove(l)
            
    for ls in lost:
        if ls==n:
            ls=0
        if ls-1 in reserve:
            have.append(ls)
            reserve.remove(ls-1)
            continue
        elif ls+1 in reserve:
            have.append(ls)
            reserve.remove(ls+1)
            
    #reserve에 남은 학생도 추가
    have+=reserve
    
    answer=len(set(have))
    return answer