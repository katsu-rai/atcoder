n, m = map(int, input().split())
chart = [[] for _ in range(n)]
ans_list = []

for i in range(n):
    chart[i] = input()

for i in range(0, n - 8):
    for j in range(0, m - 8):
        condition = (
            chart[i][j] == "#"
            and chart[i][j + 1] == "#"
            and chart[i][j + 2] == "#"
            and chart[i][j + 3] == "."
            and chart[i + 1][j] == "#"
            and chart[i + 1][j + 1] == "#"
            and chart[i + 1][j + 2] == "#"
            and chart[i + 1][j + 3] == "."
            and chart[i + 2][j] == "#"
            and chart[i + 2][j + 1] == "#"
            and chart[i + 2][j + 2] == "#"
            and chart[i + 2][j + 3] == "."
            and chart[i + 3][j] == "."
            and chart[i + 3][j + 1] == "."
            and chart[i + 3][j + 2] == "."
            and chart[i + 3][j + 3] == "."
            and chart[i + 5][j + 5] == "."
            and chart[i + 5][j + 6] == "."
            and chart[i + 5][j + 7] == "."
            and chart[i + 5][j + 8] == "."
            and chart[i + 6][j + 5] == "."
            and chart[i + 6][j + 6] == "#"
            and chart[i + 6][j + 7] == "#"
            and chart[i + 6][j + 8] == "#"
            and chart[i + 7][j + 5] == "."
            and chart[i + 7][j + 6] == "#"
            and chart[i + 7][j + 7] == "#"
            and chart[i + 7][j + 8] == "#"
            and chart[i + 8][j + 5] == "."
            and chart[i + 8][j + 6] == "#"
            and chart[i + 8][j + 7] == "#"
            and chart[i + 8][j + 8] == "#"
        )
        if condition:
            ans_list.append([i + 1, j + 1])

ans_list.sort()

for i in ans_list:
    print(f"{i[0]} {i[1]}")
