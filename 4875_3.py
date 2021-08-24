T=int(input())
for tc in range(T):
    n=int(input())
    arr=[list(map(int,input())) for i in range(n)]
    dir=[[-1,0],[1,0],[0,-1],[0,1]]
    def func(a,b):
        if arr[a][b]==3:
            return 1
        arr[a][b]=1
        for i in dir:
            na,nb=a+i[0],b+i[1]
            if 0<=na<n and 0<=nb<n and arr[na][nb]!=1:
                if func(na,nb):
                    return 1
        return 0

    for i in range(n):
        for j in range(n):
            if arr[i][j]==2:
                print(f'#{tc+1} {func(i,j)}')
                break