nums = list(map(int, input().split(",")))

max_num = 0
i = 0
while i + nums[i] < len(nums) - 1:
    for j in range(i + 1, i + nums[i] + 1):
        if max_num <= nums[j]:
            max_num = nums[j]
            k = j

    if max_num == 0:
        print(False)

    i = k

    max_num = 0

    if i >= len(nums):
        print(True)

print(True)

# nums = list(map(int, input().split(",")))

# max_num = 0
# i = 0
# while i < len(nums) - 1:
#     if nums[i] == 0:
#         print(False)

#     for j in range(2, 4):
#         max_num = max(max_num, nums[j])

#     i += max_num
#     max_num = 0

# print(True)
