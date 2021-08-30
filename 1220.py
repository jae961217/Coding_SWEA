for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    j = 0
    while j<N:
        i = 0
        while i<N-1:
            if arr[i][j] == 1:
                if arr[i+1][j]==0:
                    arr[i+1][j]=1
                elif arr[i+1][j]==2:
                    cnt+=1
            i+=1
        j+=1

    print(f'#{tc+1} {cnt}')