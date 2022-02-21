def solution(s, n):
    answer=''
    for i in s:
        c=ord(i)+n
        if i==' ':
            answer+=i
        #대문자가 Z를 넘어갈 때
        elif i.isupper() and c>ord('Z'):
            c-=ord('Z')
            #c가 1일때 'A'이므로
            answer+=chr(ord('A')+c-1)
            continue
        elif c >ord('z'):
            c-=ord('z')
            answer+=chr(ord('a')+c-1)
            continue
        else: 
            answer+=chr(c)
    return answer