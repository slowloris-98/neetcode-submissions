class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        s=s.lower()
        while l<=r:
            print(s[l], s[r])
            if not (ord('0')<=ord(s[l])<=ord('9') or ord('a')<=ord(s[l])<=ord('z') or ord('A')<=ord(s[l])<=ord('Z')):
                l+=1
                continue
            if not (ord('0')<=ord(s[r])<=ord('9') or ord('a')<=ord(s[r])<=ord('z') or ord('A')<=ord(s[r])<=ord('Z')):
                r-=1
                continue

            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
