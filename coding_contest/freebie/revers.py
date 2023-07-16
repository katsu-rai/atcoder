N = int(input())
count = 0
list_unique = []

list_str = []

for _ in range(N):
    list_str.append(input())

for i in range(N):
    if list_str[i] != list_str[j] and list_str[i] != list_str[j][::-1]:
        count += 1
        list_unique.append(list_str[i])

print(count)


#  -----------------------------
# n=int(input())
# ss=set()
# for _ in range(n):
#   s=input()
#   ss.add(min(s,s[::-1]))
# print(len(ss))
#  -----------------------------

# #
# n = int(input())
# ls_str = []
# ls_org = set()
# counter = 0
# for _ in range(n):
#     #    t_strl=list(input())
#     t_str = str(input())
#     #    t_ls_rl = list(reversed(t_strl))
#     t_ls_r = "".join(list(reversed(t_str)))
#     #    print(t_str,t_ls_r)
#     if (t_str not in ls_org) and (t_ls_r not in ls_org):
#         ls_org.add(t_str)
#         #        print(ls_org)
#         counter += 1

# print(counter)
