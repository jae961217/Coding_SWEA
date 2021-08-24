T=int(input())
for tc in range(T):
    n=int(input())
    arr = [input() for i in range(n)]
    visited=[[0 for i in range(n)] for j in range(n)]
    dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    def func(a,b):
        visited[a][b]=1
        for i in dir:
            na,nb=a+i[0],b+i[1]
            if 0<=na<n and 0<=nb<n and (arr[na][nb]=='0' or arr[na][nb]=='3') and visited[na][nb]==0:
                func(na,nb)

    for i in range(n):
        for j in range(n):
            if arr[i][j]=='2':
                func(i,j)
            if arr[i][j]=='3':
                destx,desty=i,j

    print(f'#{tc+1} {visited[destx][desty]}')