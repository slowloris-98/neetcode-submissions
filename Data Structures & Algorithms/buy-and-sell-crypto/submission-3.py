class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        left_min=[math.inf]*n
        left_min[0]=prices[0]
        right_max=[-math.inf]*n
        right_max[n-1]=prices[n-1]
        for i in range(1,n):
            left_min[i]=min(left_min[i-1], prices[i])
        
        for i in range(n-2,-1,-1):
            right_max[i]=max(right_max[i+1], prices[i])
        
        res=0
        for i in range(n):
            res=max(res,right_max[i]-left_min[i])

        return res
        
        
        # brute force
        # res=0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         curr = prices[j]-prices[i]
        #         res=max(res,curr)
        # return res
