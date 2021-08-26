T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())
    ppl = list(map(int, input().split()))

    ppl_dict = {}
    for key in ppl:
        if not key in ppl_dict:
            ppl_dict[key] = 0
        ppl_dict[key] += 1

    ans = 'Possible'
    bread = -1 * K
    for sec in range(11112):
        if sec % M == 0:
            bread += K
        if sec in ppl_dict:
            bread -= ppl_dict[sec]
            if bread < 0:
                ans = 'Impossible'
                break

    print(f'#{tc + 1} {ans}')