n = int(input())
list = list(map(int, input().split()))
count = 0
odd_is_not_found = True

while odd_is_not_found:
    for i in range(len(list)):
        if list[i] % 2 != 0:
            odd_is_not_found = False
            break

    if odd_is_not_found:
        for i in range(len(list)):
            list[i] = list[i] / 2
        count += 1

print(count)

# ------------------------------------------------------------------
# This code below did not pass maybe becase it takes some time to
# deal with a variable that has big numbers. So I should use range()
# and call a number with index.

# n = int(input())
# list = list(map(int, input().split()))
# count = 0
# odd_is_not_found = True

# while odd_is_not_found:
#     for i in list:
#         if i % 2 != 0:
#             odd_is_not_found = False
#             break

#     if odd_is_not_found:
#         for i in list:
#             i = i / 2
#         count += 1

# print(count)

N = int(input())
A = list(map(int, input().split()))
count = 0
p = True
while p:
    for i in range(len(A)):
        if A[i] % 2 == 1:
            p = False
            break
    if p:
        for i in range(len(A)):
            A[i] = A[i] / 2
        count += 1

print(count)
