import sys

str = input()
q = int(input())
command = 0
a = 1
b = 2
p = 3
command_line = []

for _ in range(q):
    command_line = list(input().split())
    command_line[a] = int(command_line[a]) - 1
    command_line[b] = int(command_line[b])

    if command_line[command] == "print":
        print(str[command_line[a] : command_line[b]])
    elif command_line[command] == "replace":
        str = str[: command_line[a]] + command_line[p] + str[command_line[b] :]
    elif command_line[command] == "reverse":
        str = (
            str[: command_line[a]]
            + str[command_line[a] : command_line[b]][::-1]
            + str[command_line[b] :]
        )

# 00:04 sec    6448 KB     761 bytes
# from enum import Enum
# import sys

# BIG_NUM = 2000000000
# MOD = 1000000007
# EPS = 0.000000001


# line = input()
# num_query = int(input())

# for loop in range(num_query):

#     input_str = list(input().split())

#     if input_str[0] == 'replace':
#         left = int(input_str[1])
#         right = int(input_str[2])
#         right += 1
#         line = line[:left] + input_str[3] + line[right:]

#     elif input_str[0] == 'reverse':
#         left = int(input_str[1])
#         right = int(input_str[2])
#         right += 1
#         line = line[:left] + line[left:right][::-1] + line[right:]

#     else: #print
#         left = int(input_str[1])
#         right = int(input_str[2])
#         right += 1
#         for i in range(left,right):
#             print(line[i],end = "")
#         print()
