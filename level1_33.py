def solution(nums):
    s_num=len(set(nums))
    if s_num<(len(nums)/2):
        return s_num
    
    return len(nums)/2