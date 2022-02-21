def solution(s):
    s=s.split()
    s2=''
    answer=[]
    for i in s:
        for j in range(len(i)):
            s2+=i[j].upper() if j==0 or j%2==0 else i[j].lower()
        answer.append(s2)
        s2=''
    answer=' '.join(answer)
    return answer