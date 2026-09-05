class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # binary search
        l,r=1,max(piles)
        res=r
        while l<=r:
            k=(l+r)//2
            t=0
            for p in piles:
                t += p//k if p%k==0 else (p//k + 1)
                if t>h:
                    l=k+1
                    break
            if t<=h:
                res = min(res, k)
                r=k-1
        return res

        
        
        
        # # brute force
        # for k in range(1,max(piles)+1):
        #     t=0
        #     for p in piles:
        #         time = p//k if p%k==0 else (p//k + 1)
        #         t+=time
        #         if t>h:
        #             break
        #     if t<=h:
        #         return k
        # return -1

        
                


