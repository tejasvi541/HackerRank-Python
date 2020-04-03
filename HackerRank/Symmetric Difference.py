s1 = set()
s2 = set()
n = input()
ls1 = list(map(int, input().split()))
k = input()
ls2 = list(map(int, input().split()))
s1.update(ls1)
s2.update(ls2)
union1 = list(s1.difference(s2))
union2 = list(s2.difference(s1))
union1.sort()
union2.sort()
ls = []
for i in range(len(union1)):
    ls.append(union1.pop(0))
for i in range(len(union2)):
    ls.append(union2.pop(0))
for i in range(len(ls)):
    print(ls.pop(0))