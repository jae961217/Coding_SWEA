T = 10
for tc in range(T):
    num,e=map(int,input().split())
    arr=[[0 for i in range(100)] for j in range(100)]
    tmp=list(map(int,input().split()))
    for i in range(0, 2*e, 2):
        arr[tmp[i]][tmp[i+1]]=1
    visited=[0]*100
    def dfs(num):
        visited[num]=1
        for i in range(100):
            if arr[num][i]==1 and not visited[i]:
                dfs(i)
    dfs(0)
    print(f'#{tc+1} {visited[99]}')