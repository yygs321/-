def solution(participant,completion):
    participant.sort()
    completion.sort()
    n=len(participant)
    for i in range(n-1):
        #순서대로인데 같지 않은 값이 나올 경우:도중에 중복값이 발생
        if participant[i]!=completion[i]:
            return participant[i]
    #completion의 값이 다 순서대로 participant에 있었던 경우: 그 다음 값이 완주하지 못한 선수
    return participant[i+1]