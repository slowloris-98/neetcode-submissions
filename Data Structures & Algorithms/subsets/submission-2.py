class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        curr=[]

        def dfs(i):
            
            res.append(curr[:])

            for j in range(i,n):
                curr.append(nums[j])    
                dfs(j+1)
                curr.pop()
                
        dfs(0)
        print(res)
        return res





            
            


