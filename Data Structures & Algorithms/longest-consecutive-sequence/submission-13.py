class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 1:
            return 1
        if not nums:
            return 0
        curr = 1
        res = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                curr += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                curr = 1
            res = max(res, curr)
        return res