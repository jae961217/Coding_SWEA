from collections import deque

for tc in range((input())):
    n, m = map(int, input().split())
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    value=0
    for i in range(n):
        tmp = input()
        for j in range(m):
            if tmp[j]=='W':
                q.append((i, j))
                dist[i][j] = 0
    while q:
        tmpx, tmpy = q.popleft()
        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = tmpx + x, tmpy + y
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny]==-1:
                q.append((nx, ny))
                dist[nx][ny] = dist[tmpx][tmpy] + 1

    for i in dist:
        for j in i:
            value+=j
    print(f'#{tc + 1} {value}')