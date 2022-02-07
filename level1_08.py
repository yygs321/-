def solution(num):
    count=0
    while num!=1:
        if count>=500:
            return -1
        else:
            num= (lambda x: x//2 if x%2==0 else x*3+1)(num)
            count+=1
        
    return count