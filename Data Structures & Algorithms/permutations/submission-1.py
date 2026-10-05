class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        curr=[]
        res=[]
        pick=[False]*n

        def dfs(curr):
            if len(curr)==n:
                res.append(curr[:])
                return
            for i in range(n):
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i]=True
                    dfs(curr)
                    curr.pop()
                    pick[i]=False
        dfs(curr)
        return res
