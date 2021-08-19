T = int(input())
for tc in range(T):
    v,e=map(int,input().split())
    arr=[[0 for i in range(v)] for j in range(v)]
    for i in range(e):
        a,b=map(int,input().split())
        arr[a-1][b-1]=1
    start,end=map(int,input().split())
    visited=[0]*v
    def dfs(num):
        visited[num]=1
        for i in range(v):
            if arr[num][i]==1 and not visited[i]:
                dfs(i)
    dfs(start-1)
    print(f'#{tc+1} {visited[end-1]}')