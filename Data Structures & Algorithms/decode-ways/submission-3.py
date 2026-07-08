class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)

        # bottom up

        dp=[1]*(n+1)

        for i in range(n-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            
            if i<n-1 and (s[i]=="1" or (s[i]=="2" and s[i+1]<"7")):
                dp[i]+=dp[i+2]
        return dp[0]


        # top down

        # cache={}

        # def dfs(i):
        #     if i==n:
        #         return 1
        #     if s[i]=="0":
        #         return 0
        #     if i in cache:
        #         return cache[i]

        #     cache[i]=dfs(i+1)

        #     if i<n-1:
        #         if s[i]=="1" or (s[i]=="2" and s[i+1]<"7"):
        #             cache[i]+=dfs(i+2)
        #     return cache[i]
        
        # return dfs(0)

