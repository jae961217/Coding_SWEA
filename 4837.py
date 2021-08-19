import sys
input=sys.stdin.readline

# Press the green button in the gutter to run the script.
def func(arr):
    for i in range(1,1<<10):
        s=0
        for j in range(10):
            if i & (1<<j):
                s+=arr[j]
                if s==0:
                    return 1
    return 0

T=int(input())
for tc in range(T):
    arr = list(map(int,input().split()))
    print(f'#{tc+1} {func(arr)}')