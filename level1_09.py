def solution(n, m):
    #유클리드 호제법
    #최대공약수
    a,b=n,m
    GCD=0
    LCM=0
    while b:
      a,b=b,a%b 
    GCD=a
    #최소공배수
    LCM= n*m // GCD
    answer=[GCD,LCM]
    return answer

print(solution(2,10))