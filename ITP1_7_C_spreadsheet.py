number_of_rows, number_of_columns = map(int, input().split())

spreadsheet = [[] for _ in range(number_of_rows + 1)]

sum_of_each_row = 0
sum_of_each_colum = 0

for row in range(number_of_rows):
    sum_of_each_row = 0
    spreadsheet[row] = list(map(int, input().split()))

    for column in range(number_of_columns):
        sum_of_each_row += spreadsheet[row][column]
        print(spreadsheet[row][column], end=" ")

    spreadsheet[row].append(sum_of_each_row)
    print(sum_of_each_row)

for column in range(number_of_columns):
    for row in range(number_of_rows):
        sum_of_each_colum += spreadsheet[row][column]

    spreadsheet[number_of_rows][column].append(sum_of_each_colum)
    sum_of_each_colum = 0

for column in range(spreadsheet[number_of_rows + 1]):
    print(column, end=" ")


# H, W = map(int, input().split())

# table = [[0] * (W + 1) for i in range(H + 1)]


# for row in range(H):
#     work = list(map(int, input().split()))  # ★★直にtableに代入すると、列数が変わってしまう!!!★★★
#     for col in range(W):
#         table[row][col] = work[col]


# for row in range(H):
#     for col in range(0, W):
#         table[row][W] += table[row][col]


# for col in range(0, W + 1):
#     for row in range(0, H):
#         table[H][col] += table[row][col]


# for row in range(0, H + 1):
#     print("%d" % (table[row][0]), end="")
#     for col in range(1, W + 1):
#         print(" %d" % (table[row][col]), end="")
#     print()
