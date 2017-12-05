# θ(n)
nums = []
nums.append(1)      # θ(1)
nums.insert(0, 2)   # θ(n)

# θ(n)
seq = []
s = 0
for x in seq:
    s += x

# θ(n)
squares = [x**2 for x in seq]

# θ(n*n)
s = 0
for x in seq:
    for y in seq:
        s += x*y

# θ(n*n*n)
s = 0
for x in seq:
    for y in seq:
        s += x*y
    for z in seq:
        for w in seq:
            s += x-w

# θ(n*m)
# seq1 contains n elemnts and seq2 contains m elemnts
s = 0
for x in seq1:
    for y in seq2:
        s += x*y

# Cannot count
seq1 = [[0, 1], [2], [3, 4, 5]]
s = 0
for seq2 in seq1:
    for x in seq2:
        s += x

# Chapter3 covered: θ(n*n)
s = 0
n = len(seq)
for i in range(n - 1):
    for j in range(i + 1, n):
        s += seq[i] * seq[j]
