T=10
for tc in range(T):
    a=int(input())
    numbers=list(map(int,input().split()))
    idx=0
    while True:
        numbers.append(numbers[0]-idx-1)
        numbers.pop(0)
        if numbers[-1]<=0:
            numbers[-1]=0
            break
        idx=(idx+1)%5
    print(f'#{tc+1}',end=' ')
    for i in numbers:
        print(i,end=' ')
    print()
