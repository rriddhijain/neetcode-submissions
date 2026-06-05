class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        r=[]
        for i in range(len(numbers)):
            j=len(numbers)-1
            comp=target-numbers[i]
            while i<j:
                if numbers[j]==comp:
                    t=j+1
                    s=i+1
                    r.append(s)
                    r.append(t)
                    break
                else:
                    j-=1
        return r