def solution(x):
    k=x
    sum=0
    n=[10000,1000,100,10]
    for i in n:
        a=x//i
        x%=i
        sum+=a
    sum+=x
    
    answer=bool(k%sum==0)
    return answer