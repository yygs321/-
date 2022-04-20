from collections import deque
def solution(prices):
    queue=deque(prices)
    answer = []
        
    while queue:
        count=0
        q=queue.popleft()
        for a in queue:
            if a<q:
                count+=1
                break
            count+=1
        answer.append(count)
        
    return answer