x_500 = int(input())
y_100 = int(input())
z_50 = int(input())
price = int(input())

ans = 0

# for i in range(x_500):
#     total_500 = 500 * i
#     for j in range(y_100):
#         total_100 = 100 * j
#         condition1 = (price - total_500 - total_100) % 50 == 0
#         condition2 = (price - total_500 - total_100) / 50 <= z_50
#         if condition1 and condition2:
#             ans += 1

for i in range(x_500 + 1):
    total_500 = 500 * i
    for j in range(y_100 + 1):
        total_100 = 100 * j
        for k in range(z_50 + 1):
            total_50 = 50 * k
            if total_500 + total_100 + total_50 == price:
                ans += 1

print(ans)
