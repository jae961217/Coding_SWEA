for tc in range(int(input())):
    n=int(input())
    tmp=list(map(int,input().split()))

    heap=[0]
    value=0
    def func(node):
        par=node//2
        if par==0:
            return
        if heap[par]>heap[node]:
            heap[par],heap[node]=heap[node],heap[par]
            func(par)
    cnt=1
    for i in tmp:
        heap.append(i)
        func(cnt)
        cnt+=1
    while n:
        n//=2
        value+=heap[n]

    print(f'#{tc+1} {value}')