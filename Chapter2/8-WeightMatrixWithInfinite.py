a, b, c, d, e, f, g, h = range(8)
inf = float('inf')


W = [[  0,   2,   1,   3,   9,   4, inf, inf],  # a
     [inf,   0,   4, inf,   3, inf, inf, inf],  # b
     [inf, inf,   0,   8, inf, inf, inf, inf],  # c
     [inf, inf, inf,   0,   7, inf, inf, inf],  # d
     [inf, inf, inf, inf,   0,   5, inf, inf],  # e
     [inf, inf,   2, inf, inf,   0,   2,   2],  # f
     [inf, inf, inf, inf, inf,   1,   0,   6],  # g
     [inf, inf, inf, inf, inf,   9,   8,   0]]  # h


# Neighborhood membership
W[a][b] < inf
W[c][e] < inf

# Degree
sum(1 for w in W[a] if w < inf) - 1
