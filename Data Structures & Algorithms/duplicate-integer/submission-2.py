class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        x = len(nums)
        for i in range(x-1):
            if nums[i+1]==nums[i]:
                return True
        return False 
