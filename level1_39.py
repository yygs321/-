def solution(board, moves):
    result=[0,]
    answer=0
    
    b=[[j for j in i] for i in board] #없어도 되는 코드
    
    for move in moves:
        for i in range(len(board)):
            if b[i][move-1]==0:
                continue
                
            #인형이 들어있을 때
            if result[-1]==b[i][move-1]: #맨 마지막 인형과 동일할 경우
                del result[-1]
                answer+=2
            else:
                result.append(b[i][move-1])
            
            b[i][move-1]=0 #뽑은 인형 칸 비우기
            break
        
    return answer