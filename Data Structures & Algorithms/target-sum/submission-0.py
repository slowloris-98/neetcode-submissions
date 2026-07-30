class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)

        def dfs(i,curr):
            if i==n: 
                if curr==target:
                    return 1
                else:
                    return 0
            
            return dfs(i+1, curr+nums[i]) + dfs(i+1, curr-nums[i])
            
        return dfs(0,0)

            




