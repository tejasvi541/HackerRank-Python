a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

for i in a:
    for k in b:
        print((i, k), end= " ")
