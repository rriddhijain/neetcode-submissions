class Solution:
    def findMin(self, nums: List[int]) -> int:
        j=0
        while j<len(nums)-1:
            if nums[j]<nums[j+1]:
                j+=1
            else:
                break
        if j==len(nums)-1:
            piv2=0
        else:
            piv2=j+1
        return nums[piv2]
        