class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=""
        strs.sort()
        n=len(strs)
        for i in range(len(strs[0])):
            if strs[0][i] != strs[n-1][i]:
                return pre
            pre+=strs[0][i]
        return pre


