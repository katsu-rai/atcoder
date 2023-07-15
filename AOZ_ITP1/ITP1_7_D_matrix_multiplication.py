n, m, l = map(int, input().split())

A_matrix = [[] for _ in range(n)]
B_matrix = [[] for _ in range(m)]
C_matrix = [[0] * l for _ in range(n)]


for i in range(n):
    A_matrix[i] = list(map(int, input().split()))

for i in range(m):
    B_matrix[i] = list(map(int, input().split()))

for x in range(n):
    for y in range(l):
        for z in range(m):
            C_matrix[x][y] += A_matrix[x][z] * B_matrix[z][y]

for x in range(n):
    for y in range(l):
        if y in range(l - 1):
            print(C_matrix[x][y], end=" ")
        else:
            print(C_matrix[x][y])
