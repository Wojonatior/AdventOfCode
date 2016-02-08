from functools import reduce
from itertools import combinations
from operator import mul

wts = [int(x) for x in open("day24input.txt","r").read().split('\n')]

def day24(num_groups):
    group_size = sum(wts) // num_groups
    for i in range(len(wts)):
        qes = [reduce(mul, c) for c in combinations(wts, i) 
              if sum(c) == group_size]
        if qes:
            return min(qes)

print(day24(3))
print(day24(4))

