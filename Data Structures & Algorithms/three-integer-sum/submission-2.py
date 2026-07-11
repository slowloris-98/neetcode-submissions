class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        hm=defaultdict(list)
        target=0
        for i,n in enumerate(nums):
            hm[n].append(i)
        print(hm)

        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                rem = target-nums[i]-nums[j]
                if rem in hm and hm[rem][-1]>j:
                    res.add(tuple(sorted([nums[i],nums[j],rem])))  
        
        return [list(t) for t in res]

        #for i in range():

