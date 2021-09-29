for tc in range(int(input())):
    s = input()
    num = []
    for i in range(10):
        tmp = s[i * 7:(i + 1) * 7][::-1]
        value = 0
        for j in range(len(tmp)):
            if tmp[j] == '1':
                value += 2 ** j
        num.append(value)

    print(f'#{tc + 1}', end=' ')
    for i in num:
        print(i, end=' ')
    print()