for tc in range(int(input())):
    prob=input().split()
    res=''
    for i in prob[1]:
        tmp=bin(int('0x'+i,16))[2:]
        while len(tmp)<4:
            tmp='0'+tmp
        res+=tmp


    print(f'#{tc+1} {res}')