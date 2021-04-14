x = 2
y = 2
z = 2
n = 2

permutationsX = [x for x in range(x+1)]
permutationsY = [y for y in range(y+1)]
permutationsZ = [z for z in range(z+1)]

print([[x, y, z]
       for x in permutationsX for y in permutationsY for z in permutationsZ
       if x + y + z != n])

