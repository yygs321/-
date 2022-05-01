def solution(s):
    result=0
    answer = True
    for i in s:
        if i=="(":
            result+=1
        elif i==")":
            result-=1
        if result<0:
            return False
    if result==0:
        return True
    return False