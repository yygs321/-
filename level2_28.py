def solution(phoneBook):
    #길이로 정렬
    phoneBook.sort(key=len)
    hash_table={}
    
    #맨 처음 가장 짧은 길이
    min_len=len(phoneBook[0])
    
    for p in phoneBook:
        hash_table[hash(p)]=p
        
        #가장 짧은 길이부터 잘라서 해시 값 찾아가기
        for i in range(min_len,len(p)): #p가 최소길이인 경우는 실행하지 X
            try:
                if hash_table[hash(p[0:i])]: #len(p)-1 까지만 검색
                    return False
            except:
                continue
    return True