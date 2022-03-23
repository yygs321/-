def solution(numbers, hand):
    answer = ''
    # *과 #은 -1, -2로 대체
    l,r=-1,-2
    x,y=0,0
    l_distance=0
    r_distance=0
    
    phone=[[1,2,3],[4,5,6],[7,8,9],[-1,0,-2]]
    
    for num in numbers:
        if num==1 or num==4 or num==7:
            answer+='L'
        elif num==3 or num==6 or num==9:
            answer+='R'
        else:
            for i in range(4):
                for j in range(3):
                    if phone[i][j]==num:
                        x,y=i,j
            for i in range(4):
                for j in range(3):
                    if phone[i][j]==l:
                        l_distance=(max(i,x)-min(i,x))+(max(j,y)-min(j,y))
                    if phone[i][j]==r:
                        r_distance=(max(i,x)-min(i,x))+(max(j,y)-min(j,y))
            #거리가 더 짧은 쪽에서 움직임
            if l_distance<r_distance:
                answer+='L'
            elif r_distance<l_distance:
                answer+='R'
            elif r_distance==l_distance:
                if hand=='left':
                    answer+='L'
                elif hand=='right':
                    answer+='R'
        #위치 저장 
        if answer[-1]=='L':
            l=num
        if answer[-1]=='R':
            r=num
            
    return answer