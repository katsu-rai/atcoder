manage_table = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]

N = int(input())

BUILDING_INDEX = None
FLOOR_INDEX = None
ROOM_INDEX = None
PERSON_NUMBER = None

for _ in range(N):
    data = list(map(int, input().split()))
    BUILDING_INDEX = data[0] - 1
    FLOOR_INDEX = data[1] - 1
    ROOM_INDEX = data[2] - 1
    PERSON_NUMBER = data[3]
    manage_table[BUILDING_INDEX][FLOOR_INDEX][ROOM_INDEX] += PERSON_NUMBER


x = 0
for i in range(4):
    if x != 0:
        print("#" * 20)
    x += 1

    for a in range(3):
        for b in range(10):
            print(" %d" % (manage_table[i][a][b]), end="")
        print()
