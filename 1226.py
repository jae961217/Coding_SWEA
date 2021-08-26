for tc in range(10):
    idx=int(input())
    arr=[input() for i in range(16)]
    visited=[[0 for i in range(16)] for j in range(16)]
    dir=[[-1,0],[1,0],[0,-1],[0,1]]
    startx,starty=0,0
    endx,endy=0,0
    for i in range(16):
        for j in range(16):
            if arr[i][j]=='2':
                startx,starty=i,j
            if arr[i][j]=='3':
                endx, endy = i, j

    def func(a,b):
        visited[a][b]=1
        for i in dir:
            na,nb=a+i[0],b+i[1]
            if (arr[na][nb]=='0' or arr[na][nb]=='3') and not visited[na][nb]:
                func(na,nb)

    func(starty,startx)

    print(f'#{tc+1} {visited[endx][endy]}')