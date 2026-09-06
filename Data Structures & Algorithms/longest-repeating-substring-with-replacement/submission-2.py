class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)

        l,r = 0,0
        fm,maxf,res= {}, 0, 0
        for r in range(n):
            fm[s[r]] = fm.get(s[r],0) + 1
            maxf = max(maxf, fm[s[r]])
            while (r-l+1)-maxf > k:
                fm[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res

        
        
        # # two pointer
        # res=0
        # for i in range(n):
        #     fm,maxf = {}, 0
        #     for j in range(n):
        #         fm[s[j]] = fm.get(s[j],0) + 1
        #         maxf = max(maxf, fm[s[j]])
        #         if (j-i+1)-maxf <=k:
        #             res=max(res,j-i+1)
        # return res