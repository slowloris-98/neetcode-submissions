class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        # prefix and postfix
        pre=1
        post=1
        j=n-1
        prod=[1]*n
        for i in range(n):
            prod[i]=prod[i]*pre
            prod[j]=prod[j]*post
            pre=pre*nums[i]
            post=post*nums[j]
            j-=1
        return prod
            
        
        
        # two pass
        '''
        res = []
        for i in range(n):
            prod=1
            for j in range(n):
                if i!=j:
                    prod*=nums[j]
            res.append(prod)
        
        return res
        '''
        
        # with division
        '''
        prod=1
        seen_zero=False
        for n in nums:
            if not seen_zero and n==0:
                seen_zero=True
                continue
            else:
                prod*=n

        for n in nums:
            if seen_zero:
                if n!=0:
                    res.append(0)
                else:
                    res.append(int(prod))
            else:
                res.append(int(prod/n))
        
        return res
        '''