def solution(number, k):
    list=[number[0]]
    for num in number[1:]:
    #앞의 값보다 큰 값이 나오면 작은 값이 없어질때까지 반복하면서 제거
        while len(list)>0 and list[-1]<num and k>0: 
            list.pop()
            k-=1
        list.append(num)
        
    if k:
        list=list[:-k]
    answer=''.join(list)

    return answer