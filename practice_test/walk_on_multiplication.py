n = int(input())
ans_x = 1000000000000000000000000000000000
ans_y = 0

for x in range(1, n + 1):
    if n % x == 0:
        for y in range(1, n + 1):
            if x * y == n:
                if x + y < ans_x + ans_y:
                    ans_x = x
                    ans_y = y

print(ans_x + ans_y - 2)

# n = int(input())

# def div(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]
# c = len(div(n))
# if(c % 2 == 1):
#     print(div(n)[c // 2] * 2 - 2)
# else:
#     print(div(n)[(c // 2) - 1] + div(n)[(c // 2)] - 2)
