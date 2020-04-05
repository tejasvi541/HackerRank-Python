# from itertools import combinations

# a, b = input().split()
# print(*[''.join(j) for i in range(1, int(b) + 1) for j in combinations(sorted(a), i)], sep='\n')
from itertools import combinations

s, n = input().split()
com_list = list()

for i in range(1, int(n) + 1):
    com_list.extend(combinations(sorted(s), i))

for each in com_list:
    print(*each, sep='')
