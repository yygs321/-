from collections import deque

def solution(priorities, location):
    answer = []
    queue=deque([i for i in range(len(priorities))])
    dic={idx:p for idx,p in enumerate(priorities)}
    
    while queue:
        key=queue.popleft()
        value=dic.get(key)
        
        if value<max(dic.values()):
            queue.append(key)
            continue
        answer.append(key)
        del dic[key]
    
    return answer.index(location)+1
