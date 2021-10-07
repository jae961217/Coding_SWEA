for tc in range(int(input())):
    n=int(input())
    queen=[0 for i in range(n)]

    def func(queen, idx):
        res = 0
        if idx==n:
            return 1
        for i in range(n):
            queen[idx]=i
            for j in range(idx):
                if queen[j]==queen[idx] or (abs(queen[j]-queen[idx])==idx-j):
                    break
            else:
                res+=func(queen,idx+1)
        return res

    print(f'#{tc+1} {func(queen,0)}')