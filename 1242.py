Conversion = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
decryption = {'211':0, '221':1, '122':2, '411':3, '132':4, '231':5, '114':6, '312':7, '213':8, '112':9}

def reduce(c, b, a):
    min_num = min(c,b,a)
    c //= min_num
    b //= min_num
    a //= min_num
    return str(c)+str(b)+str(a)

for tc in range(int(input())):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    tmp = [''] * n
    for i in range(n):
        for j in range(m):
            tmp[i] += Conversion[arr[i][j]]

    result = []
    visited = []
    ans = 0
    for y in range(n):
        a = b = c = 0
        for x in range(m * 4 - 1, -1, -1):
            if b == 0 and c == 0 and tmp[y][x] == '1':
                a += 1
            elif a > 0 and c == 0 and tmp[y][x] == '0':
                b += 1
            elif a > 0 and b > 0 and tmp[y][x] == '1':
                c += 1

            if a > 0 and b > 0 and c > 0 and tmp[y][x] == '0':
                result.append(decryption[reduce(c, b, a)])
                a = b = c = 0

            if len(result) == 8:
                result = result[::-1]
                value = (result[0] + result[2] + result[4] + result[6]) * 3 + (result[1] + result[3] + result[5]) + result[7]

                if value % 10 == 0 and result not in visited:
                    ans += sum(result)

                visited.append(result)
                result = []

    print(f'#{tc+1} {ans}')