def solution(phone_number):
    answer = "*"*(len(phone_number)-4) + phone_number[-4:]
    return answer
    
print(solution('01011112222'))
print(solution('024445555'))

#결과
#*******2222
#*****5555