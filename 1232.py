for tc in range(10):
    n=int(input())
    tree=[[0,0,0,0] for i in range(n+1)]
    for i in range(n):
        tmp=input().split()
        if tmp[1].isdigit():
            tree[int(tmp[0])][1]=int(tmp[1])
        else:
            tree[int(tmp[0])][1] = tmp[1]
            tree[int(tmp[0])][2] = int(tmp[2])
            tree[int(tmp[0])][3] = int(tmp[3])

    def func(num):
        if num>=n:
            return
        if tree[num][2]>0:
            func(tree[num][2])
        if tree[num][3]:
            func(tree[num][3])
        if tree[num][1]=='+':
            tree[num][1]=tree[tree[num][2]][1]+tree[tree[num][3]][1]
        elif tree[num][1]=='-':
            tree[num][1] = tree[tree[num][2]][1] - tree[tree[num][3]][1]
        elif tree[num][1]=='*':
            tree[num][1] = tree[tree[num][2]][1] * tree[tree[num][3]][1]
        elif tree[num][1]=='/':
            tree[num][1] = tree[tree[num][2]][1] / tree[tree[num][3]][1]

    func(1)
    print(f'#{tc+1} {int(tree[1][1])}')