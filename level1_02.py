n,m=map(int,input().split())
#가로길이가 n(열), 세로길이가 m(행)
for i in range(m):
    for j in range(n):
        print("*",end='')
    print()