for tc in range(int(input())):
    n,m,l= map(int,input().split())
    tree=[0 for i in range(n+1)]
    for i in range(m):
        node, value = map(int,input().split())
        tree[node]=value

    def func(num):
        if num>n:
            return 0
        tree[num]=func(num*2)+func(num*2+1)
        return tree[num]

    func(1)

    print(f'#{tc+1} {tree[l]}')