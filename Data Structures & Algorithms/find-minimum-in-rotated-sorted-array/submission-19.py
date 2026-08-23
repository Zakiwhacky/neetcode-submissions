class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minim = nums[0]
        mid = (l + r) // 2
        
        while l <= r:
            if nums[l] < nums[r]:
                minim = min(nums[l], minim)
                break
            mid = (l + r) // 2
            minim = min(nums[mid], minim)
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return minim
