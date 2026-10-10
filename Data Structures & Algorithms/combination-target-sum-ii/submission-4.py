class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        candidates.sort()
        res=[]
        
        def back(i,curr,currSum):
            if currSum==target:
                res.append(curr[:])
                return

            if currSum>target:
                return

            for j in range(i,n):
                if candidates[j]+currSum>target:
                    return
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                currSum+=candidates[j]
                curr.append(candidates[j])
                back(j+1,curr,currSum)
                currSum-=candidates[j]
                curr.pop()
        
        back(0,[],0)
        return res


