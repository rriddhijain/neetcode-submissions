class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right= len(heights)-1
        max_area=0

        while left<right:
            l=min(heights[left],heights[right])
            b= abs(left-right)
            area=l*b
            if area>max_area:
                max_area=area
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
            

        return max_area



        