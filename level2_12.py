def solution(n):
    start=n+1
    sum=0
    answer = 0
    while start>=1:
        for i in range(start,0,-1):
            if sum+i<n:
                sum+=i
                continue
            elif sum+i==n:
                answer+=1
            sum=0
            break
        sum=0
        start-=1     
    return answer