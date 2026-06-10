class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            target=0-nums[i]
            j=len(nums)-1
            k=i+1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while k<j:
                add=nums[k]+nums[j]
                if add>target:
                    j-=1
                if add<target:
                    k+=1
                if add==target:
                    res.append([nums[i],nums[k],nums[j]])
                    k+=1
                    j-=1
                    while k < j and nums[k] == nums[k - 1]:
                        k += 1

                    while k < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res


