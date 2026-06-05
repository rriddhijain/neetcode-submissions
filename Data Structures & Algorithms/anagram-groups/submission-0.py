from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana=defaultdict(list)
        result=[]
        for s in strs:
            s1=tuple(sorted(s))
            ana[s1].append(s)
        for value in ana.values():
            result.append(value)
        return result
            
        