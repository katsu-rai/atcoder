# set funcation turns a list into a set data type and
# compare the list using it.
# union
# intersaction
# difference
# symmetric_difference
# issubset / issuperset

N, M = map(int, input().split())

list_F = []

flag = "No"

all = []
list_F_i = []
list_F_j = []


def j_Is_In_i(Is, Js):
    flag = True

    for j in Js:
        if not j in Is:
            flag = False

    return flag


for _ in range(N):
    all.append(list(map(int, input().split())))

for i in range(N):
    P_i = all[i][0]
    C_i = all[i][1]
    for k in range(2, C_i + 2):
        list_F_i.append(all[i][k])

    for j in range(N):
        P_j = all[j][0]
        C_j = all[j][1]
        for k in range(2, C_j + 2):
            list_F_j.append(all[j][k])

    if P_i >= P_j:
        if j_Is_In_i(list_F_i, list_F_j):
            if P_i > P_j or not j_Is_In_i(list_F_i, list_F_j):
                flag = "Yes"

print(flag)
