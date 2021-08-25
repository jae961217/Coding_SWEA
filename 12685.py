T=int(input())
for tc in range(T):
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(n)]
    res=0

    def func(a,b):
        value=0
        if not m%2==0:
            mid=(m-1)//2
            value-=arr[a+mid][b+mid]
        for i in range(m):
            value+=arr[a+i][b+i]
            value+=arr[a+m-1-i][b+i]
        return value


    for i in range(n-m+1):
        for j in range(n-m+1):
            tmp=func(i,j)
            if res<tmp:
                res=tmp
    print(f'#{tc+1} {res}')