n = int(input())
TARO = 0
HANAKO = 1
tmp_line = [None, None]
TARO_points = 0
HANAKO_points = 0

for _ in range(n):
    tmp_line[TARO], tmp_line[HANAKO] = input().split()
    if tmp_line[TARO] > tmp_line[HANAKO]:
        TARO_points += 3
    elif tmp_line[TARO] < tmp_line[HANAKO]:
        HANAKO_points += 3
    elif tmp_line[TARO] == tmp_line[HANAKO]:
        TARO_points += 1
        HANAKO_points += 1

print(f"{TARO_points} {HANAKO_points}")
