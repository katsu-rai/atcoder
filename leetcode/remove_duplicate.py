class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
        # unique_nums = []
        # for i in nums:
        #     if i not in unique_nums:
        #         unique_nums.append(i)
        #     else:
        #         nums.pop(i)
            
        # print(nums)

    def removeDuplicates(self, nums):
        replace = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        return replace