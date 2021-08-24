T=int(input())
for tc in range(T):
    n=int(input())
    arr = [list(map(int,input())) for i in range(n)]
    visited=[[0 for i in range(n)] for j in range(n)]
    dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    res=0
    def func(a,b):
        global res
        if arr[a][b]==3:
            res=1
            return
        visited[a][b]=1
        for i in dir:
            na,nb=a+i[0],b+i[1]
            if 0<=na<n and 0<=nb<n and (arr[na][nb]==0 or arr[na][nb]==3) and visited[na][nb]==0:
                func(na,nb)
                if res:
                    return

    for i in range(n):
        for j in range(n):
            if arr[i][j]==2:
                func(i,j)
    print(f'#{tc+1} {res}')