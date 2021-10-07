for tc in range(int(input())):
    n,m=map(int,input().split())
    w=list(map(int,input().split()))
    t=list(map(int,input().split()))
    res=[0 for i in range(m)]
    w=sorted(w,reverse=True)
    t=sorted(t,reverse=True)

    for i in range(n):
        for j in range(m):
            if w[i]<=t[j]:
                if not res[j]:
                    res[j]=w[i]
                    break
    print(f'#{tc+1} {sum(res)}')

