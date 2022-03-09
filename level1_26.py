def solution(n, arr1, arr2):
    s=''
    answer = []
    
    for a,b in zip(arr1,arr2):
        a=format(a,'b') #숫자를 2진수로 치환: .format(숫자, 'b')
        b=format(b,'b')
        #2진수 길이 맞추기
        while len(a)<n:
            a='0'+a
        while len(b)<n:
            b='0'+b
            
        for i,j in zip(a,b):
            if (i=='0' or i==' ') and (j=='0' or j==' '):
                s+=' '
            else:
                s+='#'
        answer.append(s)
        s='' #s 초기화
                
    return answer