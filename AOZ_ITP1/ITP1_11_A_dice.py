# 0: 中央 1:南 2:東 3:西 4:北 5:裏側


class Dice:
    def __init__(self):
        self.number = [[0] for i in range(6)]

    def setNumber(self, n0, n1, n2, n3, n4, n5):
        self.number[0] = n0
        self.number[1] = n1
        self.number[2] = n2
        self.number[3] = n3
        self.number[4] = n4
        self.number[5] = n5

    def roll(self, location):
        if location == "E":
            self.setNumber(
                self.number[3],
                self.number[1],
                self.number[0],
                self.number[5],
                self.number[4],
                self.number[2],
            )
        elif location == "N":
            self.setNumber(
                self.number[1],
                self.number[5],
                self.number[2],
                self.number[3],
                self.number[0],
                self.number[4],
            )
        elif location == "S":
            self.setNumber(
                self.number[4],
                self.number[0],
                self.number[2],
                self.number[3],
                self.number[5],
                self.number[1],
            )
        elif location == "W":
            self.setNumber(
                self.number[2],
                self.number[1],
                self.number[5],
                self.number[0],
                self.number[4],
                self.number[3],
            )

    def get_Top(self):
        return self.number[0]


dice = Dice()
list_input = list(map(int, input().split()))
dice.setNumber(
    list_input[0],
    list_input[1],
    list_input[2],
    list_input[3],
    list_input[4],
    list_input[5],
)

location_array = input()
for str in location_array:
    dice.roll(str)

print(dice.get_Top())
