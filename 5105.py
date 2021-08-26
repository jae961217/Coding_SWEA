T=int(input())
for tc in range(T):
    n=int(input())
    arr=[input() for i in range(n)]
    dist=[[10001 for i in range(n)] for j in range(n)]
    visited=[[0 for i in range(n)] for j in range(n)]
    dir=[[-1,0],[1,0],[0,-1],[0,1]]
    startx,starty=0,0
    endx,endy=0,0
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='2':
                startx=i
                starty=j
            if arr[i][j]=='3':
                endx=i
                endy=j
    dist[startx][starty]=0
    q=[]
    q.append((startx,starty))
    while q:
        tmpx,tmpy=q.pop(0)
        visited[tmpx][tmpy]=1
        for i in dir:
            nx,ny=tmpx+i[0],tmpy+i[1]
            if 0<=nx<n and 0<=ny<n and (arr[nx][ny]=='0' or arr[nx][ny]=='3') and visited[nx][ny]==0:
                q.append((nx,ny))
                if dist[nx][ny]>dist[tmpx][tmpy]+1:
                    dist[nx][ny]=dist[tmpx][tmpy]+1


    if not dist[endx][endy]==10001:
        print(f'#{tc + 1} {dist[endx][endy] - 1}')
    else:
        print(f'#{tc + 1} {0}')
