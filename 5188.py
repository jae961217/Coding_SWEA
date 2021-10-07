for tc in range(int(input())):
    n=int(input())
    arr=[list(map(int,input().split())) for i in range(n)]
    directions=[[1,0],[0,1]]
    res=2000
    def func(x,y,value):
        global res
        if x==n-1 and y==n-1:
            res=min(res,value)
        for dx,dy in directions:
            nx,ny=dx+x,dy+y
            if 0<=nx<n and 0<=ny<n:
                func(nx,ny,value+arr[nx][ny])
    func(0,0,arr[0][0])
    print(f'#{tc+1} {res}')


