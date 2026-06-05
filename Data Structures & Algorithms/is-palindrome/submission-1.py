class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean=""
        for ch in s:
            if ch.isalnum():
                clean+=ch.lower()
        i=0
        j=len(clean)-1
        while i<j:
            if clean[i]==clean[j]:
                i+=1
                j-=1
            else:
                break
        if i>=j:
            return True
        else:
            return False        