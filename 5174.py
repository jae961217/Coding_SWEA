for tc in range(int(input())):
    e,n=map(int,input().split())
    tmp=list(map(int,input().split()))
    left = [0]*(e+2)
    right = [0] *(e+2)
    for i in range(0,len(tmp),2):
        par, chi = tmp[i],tmp[i+1]
        if left[par]:
            right[par]=chi
        else:
            left[par]=chi
    cnt=0
    def func(node):
        global cnt
        if node==0:
            return
        cnt+=1
        func(left[node])
        func(right[node])

    func(n)
    print(f'#{tc+1} {cnt}')