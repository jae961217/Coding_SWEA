for tc in range(int(input())):
    n=int(input())
    arr=[list(map(int,input().split())) for i in range(n)]
    res=0
    visited=[0 for i in range(n)]

    def func(idx,value):
        global res
        if idx==n:
            res=max(value,res)
            return
        if value<=res:
            return
        for i in range(n):
            if not visited[i]:
                visited[i]=1
                func(idx+1,value*arr[i][idx]/100)
                visited[i]=0
    func(0,1)
    print(f'#{tc+1} {res:.6f}')
