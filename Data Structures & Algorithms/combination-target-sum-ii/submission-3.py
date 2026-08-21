class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        res=[]
        candidates.sort()

        def dfs(i,curr,curr_sum):
            if curr_sum==target:
                res.append(curr[:])
                return

            if i==n or curr_sum>target:
                return

            # pick
            curr.append(candidates[i])
            dfs(i+1, curr, curr_sum+candidates[i])
            curr.pop()

            # not pick
            while i+1<n and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, curr, curr_sum)
        
        dfs(0,[],0)
        return res