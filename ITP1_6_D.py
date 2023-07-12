n, m = map(int, input().split())
A_matrix = [[] for _ in range(n)]
B_matrix = []

for i in range(n):
    A_matrix[i] = list(map(int, input().split()))

for _ in range(m):
    B_matrix.append(int(input()))

nomial = 0
sum_total = 0

for i in range(n):
    sum_total = 0
    for j in range(m):
        nomial = A_matrix[i][j] * B_matrix[j]
        sum_total += nomial

    print(sum_total)
