def solution(a, b):
    day=[ 'FRI','SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    list_a=[1,3,5,7,8,10,12] #31일을 가진 달
    days=0 #1월 1일과의 일수 차
    while a>=2:
        days+=b
        a-=1
        if a==2:
            b=29 #윤년: 2/29일을 둔 해
        else:
            if a in list_a:
                b=31
            else:
                b=30
    days+=b-1 #1월이면 1일과의 차이 계산을 위해 b-1만큼 더함
    days%=7
    
    return day[days]