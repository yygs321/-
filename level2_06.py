def fibo(result):
    sum=result[-2]+result[-1]
    result.append(sum)
    return sum
    
def solution(n):
    result=[0,1]
    for i in range(2,n+1):
        answer=fibo(result)
        
    return answer%1234567 #1234567로 나눈 나머지 값 요구