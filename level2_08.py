from collections import deque

def solution(A,B):
    A.sort()
    B.sort()
    sum1=0
    sum2=0
    answer = 0
    for i in range(len(A)):
        sum1+=A[i]*B[-i-1]
        sum2+=A[-i-1]*B[i]
        
    answer=min(sum1,sum2)

    return answer