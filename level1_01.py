def solution(id_list, report, k):
    n=int(len(id_list))
    count=[0]*n    #각 id당 신고당한 횟수
    answer=[0]*n   #각 id당 받을 메일 횟수
    p_result=''    #정지당한 id 담을 변수
    #신고당한 id저장할 변수
    p_id=[[] for i in range(n)]
    
    for r in report:
    	#신고자 id, 신고당한 id
        q,p=r.split()
        #id_list의 인덱스 값
        q_index=id_list.index(q)
        p_index=id_list.index(p)
        
        #같은 신고자가 이전에 동일한 id 신고한 적이 없을 경우에만 실행
        if p not in p_id[q_index]:
            count[p_index]+=1 
            p_id[q_index].append(p)  #신고자 id의 인덱스 위치에 신고 당한 id 저장
    
    for i in range(n):
    	#정지 기준 횟수를 넘으면 실행
        if count[i]>=k:
            p_result=id_list[i]
            
            #정지당한 id를 신고한 id들 찾아서 메일 전송 횟수 +1
            for j in range(n):
                if p_result in p_id[j]:
                    answer[j]+=1
    return answer