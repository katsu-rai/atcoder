m = int(input())
d_list = list(map(int, input().split()))

ans_m = 0
ans_d = 0

total = 1

for i in d_list:
    total += i

middle = total / 2

# while middle > 0:

for i in range(len(d_list)):
    middle -= d_list[i]

    if middle <= 0:
        middle += d_list[i]

        ans_m = i + 1
        ans_d = int(middle)
        break

print(f"{ans_m} {ans_d}")
