T=int(input())
for tc in range(T):
    v,e=map(int,input().split())
    visited=[0 for i in range(v)]
    dist=[0 for i in range(v)]
    edge=[[] for i in range(v)]
    for i in range(e):
        es,eg=map(int,input().split())
        edge[es-1].append(eg-1)
        edge[eg-1].append(es-1)
    s,g=map(int,input().split())
    q=[s-1]
    dist[s-1]=0
    while q:
        tmp=q.pop(0)
        visited[tmp]=1
        for i in edge[tmp]:
            if not visited[i]:
                q.append(i)
                dist[i]=dist[tmp]+1
    print(f'#{tc+1} {dist[g-1]}')