from collections import deque

for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    dist = [[1000000000 for i in range(n)] for j in range(n)]
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    dq = deque()
    dq.append((0, 0))
    dist[0][0] = 0

    while dq:
        tmpx, tmpy = dq.popleft()
        for x, y in direction:
            nx, ny = tmpx + x, tmpy + y
            if 0 <= nx < n and 0 <= ny < n:
                diff=0
                if arr[nx][ny]>arr[tmpx][tmpy]:
                    diff=arr[nx][ny]-arr[tmpx][tmpy]
                if dist[nx][ny]>dist[tmpx][tmpy]+1+diff:
                    dq.append((nx,ny))
                    dist[nx][ny]=dist[tmpx][tmpy]+1+diff


    print(f'#{tc + 1} {dist[-1][-1]}')