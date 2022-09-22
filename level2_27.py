def solution(m, musicinfos):
    max_m=0
    answer=""
    for music in musicinfos:
        minute=0
        start, end, name, s=music.split(",")
        start_h,start_m=map(int,start.split(":"))
        end_h,end_m=map(int,end.split(":"))
        
        #재생시간 측정
        if end_m>=start_m:
            minute+=(end_m-start_m)
        else:
            end_h-=1
            end_m+=60
            minute+=(end_m-start_m)
        minute+=60*(end_h-start_h)
        
    #재생시간만큼 음길이 수정
    # C# 처럼 #은 뒤의 알파벳과 하나의 음으로 생각해야한다
        n=s.count("#")
        if len(s)<=minute+n:
            s*=(minute+n//len(s)+1)
        else:
            s=s[:minute+n]

    # 기억하는 멜로디에 #이 붙은 경우 삭제 
        m2=m+"#"
        s=s.replace(m2,'')
            
        if m in s:
        	#멜로디를 가진 노래가 여러개인 경우 음이 가장 긴 것
            #시간이 같은 경우는 먼저 나온 노래를 선택하도록 시간이 길 경우에만 값 대체
            if max_m<minute:
                answer=name
                max_m= minute
                
    if answer:
        return answer
    else:
        return "(None)"