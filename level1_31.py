def solution(n):
    answer=[]
    while n>=3:
        answer.append(n%3)
        n//=3
    answer.append(n) #뒤집어진 순서로 들어감
    answer = ''.join(map(str,answer)) #숫자 리스트 문자열로 합치기
    answer=int(answer,3) #10진수로 변환
    return answer