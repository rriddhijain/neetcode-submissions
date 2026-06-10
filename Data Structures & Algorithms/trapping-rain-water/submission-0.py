class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxl=height[l]
        maxr=height[r]
        sumf=0
        while l<r:
            if height[l]<=height[r]:
                l+=1
                water=maxl-height[l]
                if water<0:
                    water=0
                maxl=max(maxl,height[l])
            else:
                r-=1
                water=maxr-height[r]
                if water<0:
                    water=0
                maxr=max(maxr,height[r])
            sumf=sumf+water
        return sumf

        

        