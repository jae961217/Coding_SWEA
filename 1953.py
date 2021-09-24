from collections import deque

for tc in range(int(input())):
    n,m,r,c,l=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(n)]
    # visited = [[0 for i in range(m)] for j in range(n)]
    dist=[[0 for i in range(m)] for j in range(n)]
    dir=[[]]
    dir.append([[-1,0],[1,0],[0,-1],[0,1]])
    dir.append([[-1,0],[1,0]])
    dir.append([[0,-1],[0,1]])
    dir.append([[-1,0],[0,1]])
    dir.append([[1,0],[0,1]])
    dir.append([[1,0],[0,-1]])
    dir.append([[-1,0],[0,-1]])
    dist[r][c]=1

    q=deque()
    q.append((r,c))

    while q:
        tmpx,tmpy=q.popleft()
        for x,y in dir[arr[tmpx][tmpy]]:
            nx,ny=tmpx+x,tmpy+y
            if 0<=nx<n and 0<=ny<m and dist[nx][ny]==0 and [-x,-y] in dir[arr[nx][ny]]:
                dist[nx][ny]=dist[tmpx][tmpy]+1
                q.append((nx,ny))
    value=0
    for i in dist:
        for j in i:
            if 0<j<=l:
                value+=1
    print(f'#{tc+1} {value}')