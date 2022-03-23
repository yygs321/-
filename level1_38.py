def solution(absolutes, signs):
    answer=sum([-a if b==False else a for a,b in zip(absolutes, signs)])
    return answer
def solution(absolutes, signs):
    answer=0
    for a,s in zip(absolutes, signs):
        if s==False:
            answer-=a
        else:
            answer+=a
    return answer