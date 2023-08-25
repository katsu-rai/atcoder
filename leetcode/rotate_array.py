nums = list(map(int, input().split(",")))
k = int(input())

temp_list = []

if k >= len(nums):
    k = k % len(nums)

temp_list = nums[-k:]


nums[k:] = nums[:-k]
nums[:k] = temp_list

print(nums)
