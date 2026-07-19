class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod=1
        seen_zero=False
        for n in nums:
            if not seen_zero and n==0:
                seen_zero=True
                continue
            else:
                prod*=n

        print(prod)

        for n in nums:
            if seen_zero:
                if n!=0:
                    res.append(0)
                else:
                    res.append(int(prod))
            else:
                res.append(int(prod/n))
        
        return res