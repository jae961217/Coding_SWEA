for tc in range(int(input())):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]
    visited = [[0 for i in range(n)] for j in range(n)]
    flag = True
    value = 0

    def func(tmpx, tmpy, cnt):
        global k, flag, value
        if cnt > value:
            value = cnt
        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = tmpx + x, tmpy + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]==0:
                if arr[tmpx][tmpy] > arr[nx][ny]:
                    visited[nx][ny]=1
                    func(nx, ny, cnt + 1)
                    visited[nx][ny]=0
                else:
                    if flag and arr[tmpx][tmpy] > arr[nx][ny] - k:
                        flag = False
                        t=arr[nx][ny]
                        arr[nx][ny]=arr[tmpx][tmpy]-1
                        visited[nx][ny] = 1
                        func(nx, ny, cnt + 1)
                        visited[nx][ny]=0
                        arr[nx][ny]=t
                        flag = True
    maxV=0
    for i in range(n):
        for j in range(n):
            if maxV<arr[i][j]:
                maxV=arr[i][j]

    for i in range(n):
        for j in range(n):
            if maxV==arr[i][j]:
                visited = [[0 for i in range(n)] for j in range(n)]
                visited[i][j]=1
                func(i,j,1)

    print(f'#{tc + 1} {value}')