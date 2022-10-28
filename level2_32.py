import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    sum=0
    answer = 0
    while scoville[0]<K:
        if len(scoville)<2:
            return -1
        min1=heapq.heappop(scoville)
        min2=heapq.heappop(scoville)
        sum=min1+min2*2
        heapq.heappush(scoville,sum)
        answer+=1
    
    return answer
