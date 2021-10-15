import heapq

for tc in range(int(input())):
    n,e=map(int,input().split())
    dist=[100000000 for i in range(n+1)]
    graph=[[] for i in range(n+1)]
    for i in range(e):
        sta,end,w=map(int,input().split())
        graph[sta].append((end,w))

    heap=[]
    heapq.heappush(heap,(0,0))
    dist[0]=0
    while heap:
        d,n=heapq.heappop(heap)
        if dist[n]<d:
            continue

        for i in graph[n]:
            cost=d+i[1]
            if cost<dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(heap,(cost,i[0]))

    print(f'#{tc+1} {dist[-1]}')