class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        d1={}
        if len(s)==len(t):
            for i in range(len(s)):
                key=s[i]
                if key in d:
                    d[key]=d[key]+1
                    continue
                else:
                    d[key]=1
            for i in range(len(t)):
                key=t[i]
                if key in d1:
                    d1[key]=d1[key]+1
                    continue
                else:
                    d1[key]=1
            return d==d1
        else:
            return False
        
        