class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # save element index in stack along with value
        n=len(temperatures)
        res=[0]*n
        stack=[]
        for i in range(n):
            while stack and stack[-1][0]<temperatures[i]:
                temperature, ele_idx = stack.pop()
                res[ele_idx]=i-ele_idx
            stack.append((temperatures[i], i))
        return res


        
        # # brute force
        # n=len(temperatures)
        # res=[]
        # for i in range(n):
        #     days=0
        #     for j in range(i+1,n):
        #         if temperatures[j]>temperatures[i]:
        #             days=j-i
        #             break
        #     res.append(days)
        # return res
                

