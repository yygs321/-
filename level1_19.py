def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda a:a[n])
    return strings