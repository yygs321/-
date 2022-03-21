from itertools import combinations

def solution(nums):
    result=1
    count=0
    com=list(combinations(nums, 3)) #조합: 리스트에서 n개씩 추출
    n_sum=[sum(a) for a in com]
    
    for n in n_sum:
        for i in range(2,n):
            if n%i==0:
                result+=1
        if result==1:
            count+=1
        result=1
    
    return count