shop = ('''Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''.split('\n'))

bossHP = 109
bossAtk = 8
BossArm = 2
myHP = 100

from itertools import combinations

weapons = [line.split() for line in shop[1:6]]
armour = [line.split() for line in shop[8:13]]
rings = [line.split() for line in shop[15:]]
armour.append([0 for i in range(4)]) # blank entry to count as none chosen
rings.extend([[0 for i in range(5)] for j in range(2)]) # same as above

def db(w, a, i): # damage per round to boss
    return max(1, int(w[2]) + int(i[0][3]) + int(i[1][3]) - 2)
def dm(w, a, i): # damage per round to me
    return max(1, 8 - int(a[3]) - int(i[0][4]) - int(i[1][4]))


print(min([int(w[1]) + int(a[1]) + int(i[0][2]) + int(i[1][2])
           for w in weapons
           for a in armour
           for i in combinations(rings, 2)
           if (bossHP//db(w,a,i)) <= (99//dm(w,a,i))]))