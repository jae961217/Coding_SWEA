for tc in range(int(input())):
    n,m=map(int,input().split())
    tmp=bin(m)[::-1][:n]
    res='ON'
    for i in tmp:
        if not i=='1':
            res='OFF'
            break

    print(f'#{tc+1} {res}')