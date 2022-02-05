def solution(arr1,arr2):
    answer=[]
    for i in range(len(arr1)):
        ans=[arr1[i][j]+arr2[i][j] for j in range(len(arr1[0]))] 
        answer.append(ans)
    return answer