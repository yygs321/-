def solution(s):
    alpha=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    x=''
    answer = ''
    for i in s:
        if i.isalpha():
            x+=i
            if x in alpha:
                answer+=str(alpha.index(x))
                x=''
        else:
            answer+=str(i)        
    return int(answer)