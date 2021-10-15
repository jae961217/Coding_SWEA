for tc in range(int(input())):
    v,e=map(int,input().split())
    costs=[]
    res=0
    parent = [i for i in range(v+1)]
    for i in range(e):
        n1,n2,w=map(int,input().split())
        costs.append((n1,n2,w))
    costs.sort(key=lambda x:x[2])

    def find(a):
        if parent[a]==a:
            return a
        parent[a]=find(parent[a])
        return parent[a]

    def union(a,b):
        pa,pb=find(a),find(b)
        if pa==pb:
            return
        elif pa<pb:
            parent[pb]=pa
        else:
            parent[pa]=pb


    for n1,n2,c in costs:
        if find(n1)!=find(n2):
            union(n1,n2)
            res+=c
    print(f'#{tc+1} {res}')
