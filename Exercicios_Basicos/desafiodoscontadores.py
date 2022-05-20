"""
0 - 10
1 - 9
2 - 8
3 - 7
4 - 6
5 - 5
6 - 4
7 - 3
8 - 2
9 - 1
"""
a = 0
cont2 = 10
while a < 9:
    print(a, ' - ', cont2)
    a += 1
    cont2 -= 1
print('===========================================')
for progressivo, regresivo in enumerate(range(10, 1, -1)):
    print(progressivo, regresivo)
