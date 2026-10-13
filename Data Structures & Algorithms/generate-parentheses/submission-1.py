class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(curr, op, cl):
            if op==cl==n:
                res.append(curr)
                return
            
            if op<n:
                dfs(curr+'(',op+1,cl)
            
            if cl<op:
                dfs(curr+')',op,cl+1)
            
        dfs("",0,0)
        return res
            
