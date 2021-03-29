x = int(input())
x = range(0, x)
y = int(input())
y = range(0, y)
z = int(input())
z = range(0, z)
n = int(input())
print(x)
permutations = []
all_permutations = []
for i, j, k in x, y, z:
    permutations.append([i, j, k])
    print(permutations)
