class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l,r=0,0
        curr=set()
        res=0
        for r in range(n):
            while s[r] in curr:
                curr.remove(s[l])
                l+=1
            curr.add(s[r])
            res=max(res,r-l+1)
        return res
            

