for tc in range(int(input())):
    n, m = map(int, input().split())
    arr = [[0 for i in range(n)] for j in range(n)]
    visited = [0 for i in range(n)]
    res = 0
    for i in range(m):
        x, y = map(int, input().split())
        arr[x - 1][y - 1] = 1
        arr[y - 1][x - 1] = 1


    def func(idx, cnt):
        global res
        res = max(res, cnt)

        for i in range(n):
            if not visited[i] and arr[idx][i]:
                visited[i] = 1
                func(i, cnt + 1)
                visited[i]=0


    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            func(i, 1)
            visited[i]=0

    print(f'#{tc + 1} {res}')