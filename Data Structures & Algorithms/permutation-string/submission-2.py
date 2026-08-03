class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1), len(s2)
        if n2<n1:
            return False
        s1 = sorted(s1)
        for i in range(n2):
            if i+n1<=n2:
                if  sorted(s2[i:i+n1])==s1:
                    return True
            else:
                break
        return False
