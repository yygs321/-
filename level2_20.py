from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    queue=deque(truck_weights)
    list=deque()
    count=[]
    num=0
    l_weight=0
    answer=0
    while queue:
        if num!=bridge_length:
            if l_weight+queue[0]<=weight:
                t=queue.popleft()
                list.append(t)
                l_weight+=t
                count.append(0)
                if num:
                    answer+=count[-2] #앞서 건너는 트럭과의 거리 차이만큼 시간 소요
                else:
                    answer+=bridge_length #다리 제일 앞에 있는 트럭이 소요할 시간
                    
                num+=1
        for i in range(len(count)):
            count[i]+=1

        if count[0]==bridge_length:
            num-=1
            t=list.popleft()
            l_weight-=t
            del count[0]
            
    answer+=1 #맨 마지막 트럭이 나오는 시간
        
    return answer