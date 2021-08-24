T=int(input())
for tc in range(T):
    exp=input().split()
    res=0
    stack=[]
    for i in exp:
        if i=='.':
            break
        elif i.isnumeric():
            stack.append(int(i))
        else:
            if len(stack)<2:
                res=-1
                break
            else:
                sec=stack.pop()
                fir=stack.pop()
                if i=='+':
                    stack.append(fir+sec)
                elif i=='-':
                    stack.append(fir-sec)
                elif i=='*':
                    stack.append(fir*sec)
                elif i=='/':
                    stack.append(fir//sec)

    if res==-1 or len(stack)>1:
        print(f'#{tc+1} error')
    else:
        print(f'#{tc + 1} {stack[0]}')