def sub():
    s1 = set()
    s2 = set()
    n = input()
    ls1 = list(map(int, input().split()))
    k = input()
    ls2 = list(map(int, input().split()))
    s1.update(ls1)
    s2.update(ls2)
    union = list(s1.union(s2))
    cout = 0
    while union:
        union.pop()
        cout = cout + 1
    print(cout)


sub()