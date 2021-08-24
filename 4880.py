def win(x, y):
    if card[x-1]==card[y-1]:
        return x
    elif card[x-1]==1 and card[y-1]==3:
        return x
    elif card[x-1]==2 and card[y-1]==1:
        return x
    elif card[x-1]==3 and card[y-1]==2:
        return x
    return y

def match(start, end):
    if start == end:
        return start
    fir = match(start, (start+end)//2)
    sec= match((start+end)//2+1, end)
    return win(fir, sec)

T = int(input())
for tc in range(T):
    n = int(input())
    card = list(map(int, input().split()))
    print(f'#{tc+1} {match(1, n)}')