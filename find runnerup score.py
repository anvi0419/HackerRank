if _name_ == '_main_':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    l.sort(reverse=True)
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
print(l1[1])
