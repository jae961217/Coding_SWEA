T=10
for tc in range(T):
    num=int(input())
    exp=input()
    postfix=[]
    op=[]
    for i in exp:
        if i=='+':
            if op and op[-1]=='*':
                while op:
                    postfix.append(op.pop())
            op.append(i)
        elif i=='*':
            op.append(i)
        else:
            postfix.append(i)
    while op:
        postfix.append(op.pop())
    stack=[]
    for i in postfix:
        if i=='*':
            stack.append(stack.pop()*stack.pop())
        elif i=='+':
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(int(i))
    print(f'#{tc+1} {stack[0]}')