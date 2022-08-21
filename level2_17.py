def solution(n):
    answer = 0
    m=format(n,'b').count('1')
    i=n
    while True:
        i+=1
        if format(i,'b').count('1')==m:
            answer=i
            break
        
    return answer