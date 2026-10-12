class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=set()
        curr=[]

        def dfs(i):
            res.add(tuple(curr[:]))

            for j in range(i,n):
                curr.append(nums[j])
                dfs(j+1)
                curr.pop()
        
        dfs(0)
        #print(res)
        res=list(res)
        #res1=[list(item) for item in res]
        #print(res1)
        
        return res
