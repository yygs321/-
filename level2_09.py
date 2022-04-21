def solution(s):
    st=''
    result=[]
    for i in range(len(s)):
        if s[i]==" ":
            result.append(int(st))
            st=''
        st+=s[i]
        if i==len(s)-1:
            result.append(int(st))
        
    answer='{0} {1}'.format(min(result), max(result))
    return answer