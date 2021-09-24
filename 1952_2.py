for tc in range(int(input())):
    d,m,q,y = map(int, input().split())
    months = list(map(int, input().split()))
    value = y

    def price(n, s):
        global value
        if n > 11:
            if s < value:
                value = s
        elif s >= value:
            return
        else:
            res = min(months[n] * d, m)
            price(n + 1, s + res)
            price(n + 3, s + q)

    price(0, 0)
    print(f'#{tc+1} {value}')