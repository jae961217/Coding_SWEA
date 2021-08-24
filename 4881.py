T = int(input())
for tc in range(T):
    n = int(input())
    arr=[list(map(int,input().split())) for i in range(n)]
    check=[]
    value=10000
    def func(idx):
        global value
        if len(check)==n:
            tmp=0
            for i in range(len(check)):
                tmp+=arr[i][check[i]]
            value=min(value,tmp)
            return

        for i in range(n):
            if check and i in check:
                continue
            check.append(i)
            func(idx+1)
            check.pop()
    func(0)
    print(f'#{tc+1} {value}')