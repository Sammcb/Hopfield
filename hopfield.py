# Get the memory matrix from learned patterns l
def mem_matrix(l):
  return [[0 if i == j else sum([p[i] * p[j] for p in l]) for j in range(len(l[0]))] for i in range(len(l[0]))]

# Get resulting pattern from memory matrix m and new pattern p
def check_mem(m, p):
  return [sum([m[i][j] * p[j] for j in range(len(p))]) // abs(sum([m[i][j] * p[j] for j in range(len(p))])) for i in range(len(p))]

# Learned patterns
l = [
  [-1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1],
  [1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1]
]

# New pattern
p = [-1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1]

m = mem_matrix(l)
[print(row) for row in m]

print()

x = check_mem(m, p)
print(x)
