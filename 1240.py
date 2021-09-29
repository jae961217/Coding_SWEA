for tc in range(int(input())):
    n,m=map(int,input().split())
    s=''
    for i in range(n):
        tmp=input()
        if '1' in tmp:
            s=tmp[::-1]
            idx=s.index('1')
            s=s[idx:idx+56][::-1]

    code=[[3,2,1,1],[2,2,2,1],[2,1,2,2],[1,4,1,1],[1,1,3,2],[1,2,3,1],[1,1,1,4],[1,3,1,2],[1,2,1,3],[3,1,1,2]]
    validation=0
    res=0
    for i in range(8):
        check=s[i*7:(i+1)*7]
        value='0'
        cnt=1
        num=[]
        for j in range(1,7):
            if check[j]==value:
                cnt+=1
            else:
                value=check[j]
                num.append(cnt)
                cnt=1
        num.append(cnt)
        if i%2==0:
            validation+=code.index(num)*3
        else:
            validation+=code.index(num)
        res+=code.index(num)

    if not validation%10==0:
        res=0
    print(f'#{tc+1} {res}')