for tc in range(int(input())):
    numbers=list(map(int,input().split()))
    res=0
    one=dict()
    two=dict()
    for i in range(len(numbers)):
        if i%2==0:
            if not numbers[i] in one:
                one[numbers[i]]=0
            one[numbers[i]]+=1
            if one[numbers[i]]==3:
                res=1
                break
            if (numbers[i]-2) in one and (numbers[i]-1) in one:
                res=1
                break
            if (numbers[i]-1) in one and (numbers[i]+1) in one:
                res=1
                break
            if (numbers[i]+1) in one and (numbers[i]+2) in one:
                res=1
                break
        else:
            if not numbers[i] in two:
                two[numbers[i]]=0
            two[numbers[i]]+=1
            if two[numbers[i]] == 3:
                res = 2
                break
            if (numbers[i]-2) in two and (numbers[i]-1) in two:
                res=2
                break
            if (numbers[i]-1) in two and (numbers[i]+1) in two:
                res=2
                break
            if (numbers[i]+1) in two and (numbers[i]+2) in two:
                res=2
                break
    print(f'#{tc+1} {res}')