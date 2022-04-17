def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        ans=[]
        for j in range(len(arr2[0])):
            sum=0
            for k in range(len(arr2)):
                sum+=arr1[i][k]*arr2[k][j]
            ans.append(sum)
        answer.append(ans)
    return answer