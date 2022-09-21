def solution(msg):
    #아스키코드 대문자 65~90/ 소문자 97~122
    dic=[chr(64+i) if i!=0 else 0 for i in range(27) ]
    answer=[]
    word=''
    
    for i,m in enumerate(msg):
        word+=m
        if i==len(msg)-1:
            answer.append(dic.index(word))
            break
            
        if word not in dic:
            dic.append(word)
            answer.append(dic.index(word))
        else:
            if word+msg[i+1] in dic:
                continue
            else:
                answer.append(dic.index(word))
                word+=msg[i+1]
                dic.append(word)
                word=''
        
    return answer