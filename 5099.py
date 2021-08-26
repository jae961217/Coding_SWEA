T=int(input())
for tc in range(T):
    n,m=map(int,input().split())
    numbers=list(map(int,input().split()))
    q=[]
    idx=n
    for i in range(n):
        q.append((numbers[i],i+1))
    while q:
        res=q.pop(0)
        if res[0]//2:
            q.append((res[0] // 2, res[1]))
        elif res[0]//2==0 and idx<len(numbers):
            q.append((numbers[idx], idx + 1))
            idx += 1
    print(f'#{tc+1} {res[1]}')