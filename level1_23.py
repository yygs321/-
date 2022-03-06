def solution(dartResult):
    n=0 #계산할 점수
    answer=0
    first=0 #바로 전에 얻은 점수
    second=0 #해당 점수
    ten=0 #숫자 10을 인식하기 위한 값(1,0 따로 읽는 것 방지하기 위함)
    count=0
    
    for dr in dartResult:
        count+=1     
        if dr.isdigit():
            if dr=='1':
                ten=1
            elif dr=='0':
                if ten==1:
                    dr=10   
            n=int(dr)
        elif dr.isalpha():
            ten=0 #알파벳이 나오면 숫자 10이 아니므로 
            if dr=='S':
                n**=1
            elif dr=='D':
                n**=2
            elif dr=='T':
                n**=3
            #변경된 n값을 *계산을 위해 저장
            if count==1:
                first=n
            elif count==2:
                second=n
            else:
                first=second
                second=n
            #옵션이 없을 수 있으니 미리 더함
            answer+=n

        if dr=='*':
            #더했던 이전 값과 현재 값을 빼고 2배한 값으로 다시 더함
            answer-=(first+second)
            #first, second가 2배된 값으로 저장되어야 하므로 값 변경 후 더함
            first*=2
            second*=2
            answer+=(first+second)
            
        elif dr=='#':
            #더한 값 취소하고 -1배한 값으로 다시 더함
            answer-=n                
            n*=(-1)
            answer+=n
            #변경된 n값을 *계산을 위해 저장
            if count==1:
                first=n
            elif count==2:
                second=n
            else:
                first=second
                second=n
        
    return answer