class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)

        if n==0:
            return 0

        res=1
        nums_set = set(nums)
        for num in nums:
            if num-1 in nums_set:
                continue

            curr=1
            while num+curr in nums_set:
                curr+=1
                res=max(res,curr)
        return res
            





        # if n==0:
        #     return 0
        
        # if n==1:
        #     return 1

        # nums.sort()

        # i=0
        
        # res, curr = 1,1
        # while i+1<n:
        #     if nums[i+1]==nums[i]+1:
        #         curr+=1
        #         res = max(res,curr)
        #     else:
        #         curr=1
            
        #     i+=1

        #     while i+1<n and nums[i+1]==nums[i]:
        #         i+=1

        # return res
        
            
