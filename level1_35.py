def solution(answers):
    score=[0,0,0]
    result=[]
    one=[1,2,3,4,5]*(len(answers)//5+1)
    two=[2,1,2,3,2,4,2,5]*(len(answers)//8+1)
    three=[3,3,1,1,2,2,4,4,5,5]*(len(answers)//10+1)
    for i in range(len(answers)):
        ans=answers[i]
        if ans==one[i]:
            score[0]+=1
        if ans==two[i]:
            score[1]+=1
        if ans==three[i]:
            score[2]+=1
    
    m_score=score.count(max(score))
    for i in range(m_score):
        index_s=score.index(max(score))
        result.append(index_s+1)
        score[index_s]=0
        
    result=list(set(result))
    return result