def solution(n):
    answer = 0
    arr=[1]*n
    num=1
    while len(arr)>=n//2:
        c=arr.count(2)
        if c==0 or c==len(arr):
            answer+=1
        else:
            for i in range(1,c+1):
                num*=len(arr)+1-i
                num//=i 

            answer+=num
            num=1
        
        if 1 not in arr:
            break
        arr.remove(1)

        for i in range(len(arr)):
            if arr[i]==1:
                arr[i]+=1
            if sum(arr)<n:
                continue
            elif sum(arr)==n:
                break
        else:
            break
        
    return answer%1234567