class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)

        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits
        
        
        
        # num_s = ""
        # for d in digits:
        #     num_s+=str(d)
        # print(num_s)

        # num = str(int(num_s)+1)
        # res=[]
        # for c in num:
        #     res.append(int(c))

        # return res
        
        
            
