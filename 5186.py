for tc in range(int(input())):
    num=float(input())
    idx=-1
    res=''
    while True:
        if num==0:
            break
        if idx<-12:
            res='overflow'
            break
        if num>=2**idx:
            num-=2**idx
            res+='1'
        else:
            res+='0'
        idx-=1

    print(f'#{tc+1} {res}')