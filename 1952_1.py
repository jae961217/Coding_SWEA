for tc in range(int(input())):
    d, m, t, y = map(int,input().split())
    month=list(map(int,input().split()))

    value=[10000000 for i in range(len(month))]
    value[0]=min(d*month[0],m)
    for i in range(1,len(month)):
        day_v = d*month[i]
        if i==2:
            value[i]=t
        value[i]=min(value[i-1]+day_v,value[i-1]+m,value[i])
        if i>2:
            value[i]=min(value[i],value[i-3]+t)

    if value[-1]>y:
        value[-1]=y
    print(value)
    print(f'#{tc+1} {value[-1]}')