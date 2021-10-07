from itertools import permutations as p

for tc in range(int(input())):
    n=int(input())
    arr=[list(map(int,input().split())) for i in range(n)]
    check=[i for i in range(1,n)]
    res=10000
    for i in p(check,len(check)):
        value=arr[0][i[0]]
        for j in range(1,len(i)):
            value+=arr[i[j-1]][i[j]]
        value+=arr[i[-1]][0]
        res=min(res,value)
    print(f'#{tc+1} {res}')

