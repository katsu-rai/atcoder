class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    nums = list(map(int, input().split(",")))
    i = 0
    count = 0

    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            count += 1
            if count >= 2:
                nums.pop(i)
                i -= 1

        elif nums[i] != nums[i + 1]:
            count = 0

        i += 1

    print(nums)
