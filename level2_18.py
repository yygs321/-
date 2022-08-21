from collections import deque
def solution(n, t, m, p):
    answer = ''
    queue=deque('0') #가장 첫번 째 값 0
    num=0
    count=1
    def jinsu(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return jinsu(q, base) + arr[r]
    
    while t>0:
        if not queue:
            num+=1
            queue+=jinsu(num,n)
        else:
            if count==p:
                if count==m:
                    count=1
                else:
                    count+=1
                answer+=queue.popleft()
                t-=1
            else:
                if count==m:
                    count=1
                else: 
                    count+=1
                queue.popleft()

    return answer