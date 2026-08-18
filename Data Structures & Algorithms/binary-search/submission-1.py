class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        i = round(len(nums)/2)
        i2 = 0
        while nums[i] != target:
            i2 = i
            if nums[i] < target:
                l = i
            if nums[i] > target:
                r = i
            i = round((l + r) / 2)
            if i == i2 or i > len(nums)-1:
                return -1
        return i