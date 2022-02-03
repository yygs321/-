def solution(numbers):
    #사전 값으로 정렬
    numbers_str=[str(num) for num in numbers]
    #number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    numbers_str.sort(key=lambda num: num*3, reverse=True)
    
    return str(int(''.join(numbers_str)))
    #만약 numbers=[0,0,0,0]이면 0으로 나와야 하므로 int 처리
    #join한 값을 int로 만들어 준 후 요구하는 return 값인 str로 변환