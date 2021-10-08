for tc in range(int(input())):
    two=input()
    three=input()
    res=0
    money=set()

    for i in range(len(two)):
        tmp=two[:i]
        if two[i]=='1':
            tmp+='0'
        else:
            tmp+='1'
        tmp+=two[i+1:]
        m=int(tmp,2)
        money.add(m)

    for i in range(len(three)):
        tmp1=three[:i]
        tmp2=three[:i]
        if three[i]=='0':
            tmp1+='1'
            tmp2+='2'
        elif three[i]=='1':
            tmp1+='0'
            tmp2+='2'
        else:
            tmp1+='0'
            tmp2+='1'
        tmp1+=three[i+1:]
        tmp2+=three[i+1:]
        m1=int(tmp1,3)
        m2=int(tmp2,3)
        if m1 in money:
            res=m1
            break
        if m2 in money:
            res=m2
            break
    print(money)
    print(f'#{tc+1} {res}')