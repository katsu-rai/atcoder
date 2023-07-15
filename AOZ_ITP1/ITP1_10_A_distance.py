import math

x1, y1, x2, y2 = map(float, input().split())

height = y2 - y1
width = x2 - x1

answer = math.sqrt(height * height + width * width)
print(answer)
