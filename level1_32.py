def solution(left, right):
    answer=0
    for i in range(left,right+1):
        count=1 #자기 자신을 약수로 가짐
        for j in range(1,i//2+1): #자기자신을 제외하고 값//2 이상의 약수는 없다
            if i%j==0:
                count+=1
            continue
        if count%2==0:
            answer+=i
        else:
            answer-=i
        
    return answer