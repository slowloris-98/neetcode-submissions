class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]

        def back(i,curr,currSum):
            if currSum==target:
                res.append(curr[:])
                return 
            for j in range(i,n):
                if nums[j]+currSum>target:
                    return
                else:
                    currSum+=nums[j]
                    curr.append(nums[j])
                    back(j,curr,currSum)
                    curr.pop()
                    currSum-=nums[j]


        back(0,[],0)
        
        return res