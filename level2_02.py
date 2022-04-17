def solution(arr):
    arr.sort(reverse=True)
    answer=arr[0]
    for a in arr:
        if a==arr[0]:
            continue
        for i in range(1,a+1):
            if (answer*i)%a==0:
                answer=answer*i
                break
    return answer