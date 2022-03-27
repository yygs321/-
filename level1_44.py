def solution(lottos, win_nums):
    h,l=0,0 #최고로 맞은 개수, 최저로 맞은 개수
    list=[6,6,5,4,3,2,1]
    answer=[]
    for lotto in lottos:
        if lotto in win_nums:
            l+=1 
            h+=1
        if lotto==0:
            h+=1
    answer.append(list[h]) #최고순위
    answer.append(list[l]) #최저순위
    
    return answer