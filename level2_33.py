from itertools import permutations

def solution(numbers):
    answer = 0
    num1=[i for i in str(numbers)]
    num=num1
    for i in range(2,len(num1)+1):
        num=num+list(permutations(num1,i))

    num=list(set(int("".join(m)) for m in num))
    
    for n in num:
        n=int(n)
        if n==0 or n==1:
            continue

        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            answer+=1
       
    return answer