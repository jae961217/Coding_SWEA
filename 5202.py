for tc in range(int(input())):
    n=int(input())
    timetable=[]
    for i in range(n):
        s,e=map(int,input().split())
        timetable.append((s,e))
    timetable=sorted(timetable,key=lambda x:x[1])
    index, res=0, 0
    while True:
        tmp=index+1
        while tmp<len(timetable) and timetable[tmp][0]<timetable[index][1]:
            tmp+=1
        if tmp>len(timetable):
            break
        else:
            res+=1
            index=tmp

    print(f'#{tc+1} {res}')
