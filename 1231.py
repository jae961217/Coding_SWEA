for tc in range(10):
    n = int(input())
    alpha=dict()
    sub=[[] for i in range(n+1)]
    for i in range(n):
        tmp=input().split()
        alpha[int(tmp[0])]=tmp[1]
        if len(tmp)>2:
            for j in range(2,len(tmp)):
                sub[int(tmp[0])].append(int(tmp[j]))
    print(f'#{tc+1}',end=' ')
    def func(a):
        if a<=n:
            func(a*2)
            print(alpha[a],end='')
            func(a*2+1)
    func(1)
    print()

