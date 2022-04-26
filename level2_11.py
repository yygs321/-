import math
from collections import deque
def solution(fees, records):
    IN=[]
    OUT=[]
    minute=0
    answer = []
    carIO=[]
    for r in records:
        t,n,io=r.split() #입/출차 시간, 차량 번호, IN/OUT 기록
        if io=="IN":
            IN.append([n,t])
            carIO.append(n)
        else:
            OUT.append([n,t])
            carIO.remove(n)
            
    if carIO: #출차 안한 차들 23:59로 OUT기록 넣기
        for c in carIO:
            OUT.append([c,"23:59"])       
            
    IN.sort(key=lambda x:x[0])
    OUT.sort(key=lambda x:x[0])
            
    for i in range(len(IN)):
        result=0
        h1,m1=IN[i][1].split(":")
        h2,m2=OUT[i][1].split(":")
        h1,m1,h2,m2=int(h1),int(m1),int(h2),int(m2)
        if m2>=m1:
            minute+=(m2-m1)+(h2-h1)*60
        else:
            h2-=1
            m2+=60
            minute+=(m2-m1)+(h2-h1)*60
        
        if i<len(IN)-1 and IN[i][0]==IN[i+1][0]: #같은 번호가 다시 들어온 기록이 있을 경우 시간 합쳐서 계산
            continue
        else: #같은 번호가 또 없을 경우
            if minute<=fees[0]:
                answer.append(fees[1])
            else:
                minute-=fees[0]
                result=fees[1]+ math.ceil(minute/fees[2])*fees[3] #올림
                answer.append(result)
            minute=0
            
    return answer