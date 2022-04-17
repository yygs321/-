def solution(s):
    ans=[s[i].upper() if s[i-1].isalnum()==False else s[i].lower() for i in range(len(s))]
    ans[0]=ans[0].upper()
    answer=''.join(ans)
    return answer