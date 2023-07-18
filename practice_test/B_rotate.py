n = int(input())
table = [[0] * n for _ in range(n)]
last_column = 0

for i in range(n):
    tmp_line = input()
    for j, k in enumerate(tmp_line):
        table[i][j] = k

last_column = table[0][n - 1]

for i in reversed(range(n)):
    table[0][i] = table[0][i - 1]

for i in range(n):
    try:
        table[i][0] = table[i + 1][0]
    except:
        table[n - 1][0] = table[n - 1][1]

for i in range(n):
    try:
        table[n - 1][i] = table[n - 1][i + 1]
    except:
        table[n - 1][n - 1] = table[n - 2][n - 1]

for i in reversed(range(n)):
    if i != 0:
        table[i][n - 1] = table[i - 1][n - 1]

table[1][n - 1] = last_column

for i in range(n):
    if i != 0:
        print()
    for j in range(n):
        print(table[i][j], end="")
