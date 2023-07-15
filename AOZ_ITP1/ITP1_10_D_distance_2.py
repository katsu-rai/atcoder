import math

n = int(input())
list_x = list(map(int, input().split()))
list_y = list(map(int, input().split()))

p_1 = 0
p_2 = 0
p_3 = 0
p_infi = 0
p_infi_tmp = 0

for i in range(n):
    p_1 += abs(list_x[i] - list_y[i])

    p_2 += abs(list_x[i] - list_y[i]) * abs(list_x[i] - list_y[i])

    p_3 += (
        abs(list_x[i] - list_y[i])
        * abs(list_x[i] - list_y[i])
        * abs(list_x[i] - list_y[i])
    )

    p_infi_tmp = abs(list_x[i] - list_y[i])
    if p_infi_tmp > p_infi:
        p_infi = p_infi_tmp


p_2 = math.sqrt(p_2)
p_3 = p_3 ** (1 / 3)

print(p_1)
print(p_2)
print(p_3)
print(p_infi)
