class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # 2 pointer
        n=len(heights)
        l,r=0,n-1
        res=0
        while l<r:
            water = (r-l)*min(heights[l],heights[r])
            res=max(res,water)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res
        
        # # brute force calculate the amount of water for all combinations
        # n=len(heights)
        # res=0
        
        # for i in range(n):
        #     for j in range(i+1, n):
        #         water = (j-i)*min(heights[i], heights[j])
        #         res=max(res,water)
        # return res
