def solution(progresses, speeds):
    day=[]
    answer=[]
    for p,s in zip(progresses, speeds):
        remain=100-p
        if remain%s!=0: 
            day.append(remain//s+1)
        else:
            day.append(remain//s)
    
    for idx,d in enumerate(day):
        if idx==0:
            last=d
            answer.append(1)
            continue
        if d<=last:
            answer[-1]+=1
        else:
            answer.append(1)
            last=d
            
    return answern