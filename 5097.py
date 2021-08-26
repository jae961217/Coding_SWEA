T=int(input())
for tc in range(T):
    n,m=map(int,input().split())
    numbers=list(map(int,input().split()))

    print(f'#{tc+1} {numbers[m%n]}')
