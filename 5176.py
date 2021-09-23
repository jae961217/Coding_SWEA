for tc in range(int(input())):
    n=int(input())

    tree=[0 for i in range(n+1)]
    
    def func(num):
        global number
        if num<=n:
            func(2*num)
            tree[num]=number
            number+=1
            func(2*num+1)

    number=1
    func(1)
    print(f'#{tc+1} {tree[1]} {tree[n//2]}')


