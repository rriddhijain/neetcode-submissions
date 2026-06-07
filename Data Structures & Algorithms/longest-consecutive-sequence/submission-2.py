class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest = 1
        value = 1

        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]

            if diff == 1:
                value += 1
            elif diff > 1:
                longest = max(longest, value)
                value = 1

        longest = max(longest, value)

        return longest