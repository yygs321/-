def solution(brown, yellow):
    total=brown+yellow
    answer = []
    for y_r in range(yellow,0,-1):
        r=y_r+2
        if total%r!=0: 
            continue
        c=total//r
        y_c=c-2
        if (y_r+y_c)*2+4==brown:
            answer.append(r)
            answer.append(c)
            break
    return answer