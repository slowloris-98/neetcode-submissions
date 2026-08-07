class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_s = ""
        for d in digits:
            num_s+=str(d)
        print(num_s)

        num = str(int(num_s)+1)
        res=[]
        for c in num:
            res.append(int(c))

        return res
        
        
            
