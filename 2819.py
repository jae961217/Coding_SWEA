for tc in range(int(input())):
    res=set()
    arr=[input().split() for i in range(4)]
    direction=[[-1,0],[1,0],[0,-1],[0,1]]
    def func(x,y,idx,value):
        if idx==7:
            res.add(value)
            return

        for dx,dy in direction:
            nx,ny=x+dx,y+dy
            if 0<=nx<4 and 0<=ny<4:
                func(nx,ny,idx+1,value+arr[nx][ny])

    for i in range(4):
        for j in range(4):
            func(i,j,1,arr[i][j])

    print(f'#{tc+1} {len(res)}')
