from collections import deque

def solution(n, k):
    answer =0
    result=''
    queue=deque()
    while n > 0:
        n, mod = divmod(n, k)
        result=''.join(queue)
        if mod==0:
            if not result or result=='1': #null이면
                queue.clear()
                continue
            for i in range(2,int(int(result)**0.5)+1):
                if int(result)%i==0:
                    queue.clear()
                    break
            else:
                answer+=1    
                queue.clear()
        else:
            queue.appendleft(str(mod))
            
    result=''.join(queue)
    if result: #P로 끝나는 경우
        for i in range(2,int(int(result)**0.5)+1):
            if int(result)%i==0:
                break
        else:
            answer+=1
            
    return answer