def solution(array, commands):
    answer=[]
    arr=[]
    for com in commands:
        i=com[0]
        j=com[1]
        k=com[2]
        for n in range(i-1,j):
            arr.append(array[n])  
        arr.sort()
        answer.append(arr[k-1])
        for m in range(len(arr)):
            arr.pop()
    return answer