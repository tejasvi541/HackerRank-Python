from itertools import combinations_with_replacement

s, n = input().split(" ")
n = int(n)
s = list(s)

a = sorted(list(combinations_with_replacement(s, n)))
b = []
for i in range(len(a)):
    b.append(list(sorted(a[i])))
b.sort()

for i in range(len(b)):
    print(''.join(b[i]))