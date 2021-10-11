for tc in range(int(input())):
    n=int(input())
    day=list(map(int,input().split()))
    res=10000000
    for i in range(len(day)):
        if day[i]==1:
            tmp,cnt,idx=n-1,1,i
            while tmp:
                idx+=1
                idx%=7
                cnt+=1
                if day[idx]==1:
                    tmp-=1
            res=min(res,cnt)

    print(f'#{tc+1} {res}')