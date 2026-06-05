class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        flag=0
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                flag+=1
                return True
        if flag==0:
            return False
        
        