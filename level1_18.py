def solution(n):
    answer=0
    if n>=2:
        answer+=1 #2일 경우
        #짝수일 경우는 고려X
        for i in range(3,n+1,2):
            for j in range(3,int(i**0.5)+1,2):
                if i%j==0: #i의 제곱근 이하의 수 중에 약수의 경우
                    answer-=1
                    break
            answer+=1
    return answer