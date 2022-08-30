import math

def solution(n, words):
    answer=[]
    ex=[]
    
    last=words[0][0]
    for i,w in enumerate(words):
        if len(w)<2:
            return [0,0]
            
        if w[0]!=last:
            j=i+1
            if j%n==0:
                answer.append(n)
            else:
                answer.append(j%n)
            answer.append(math.ceil(j/n))
            break
        
        if w in ex:
            j=i+1 #인덱스말고 순서값
            
            if j%n==0:
                answer.append(n)
            else:
                answer.append(j%n)
            answer.append(math.ceil(j/n))
            break
            
        last=w[-1]
        ex.append(w)
        
    else:
        return [0,0]

    return answer
