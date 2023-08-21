nums = list(map(int, input().split(",")))

max = -1

nums = list(map(str, nums))

for i in nums:
    for j in nums:
        if i[::-1] == j:
            i = int(i)
            j = int(j)
            sum = i + j
            i = str(i)
            j = str(j)
            if max < sum:
                max = sum

print(max)

# class Solution:
#     def maxSum(self, nums: List[int]) -> int:
#         max = -1

#         nums = list(map(str, nums))

#         for i in nums:
#             for j in nums:
#                 if int(i) > 9:
#                     if i[::-1] == j:
#                         i = int(i)
#                         j = int(j)
#                         sum = i + j
#                         i = str(i)
#                         j = str(j)
#                         if max < sum:
#                             max = sum

#         return max
