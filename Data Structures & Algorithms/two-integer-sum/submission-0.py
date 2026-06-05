class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement=defaultdict(list)
        for i in range(len(nums)):
            num = nums[i]
            comp=target-num
            if comp in complement:
                return [complement[comp], i]
            complement[num]=i