import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # recursion
        def dfs():
            t = tokens.pop()
            if t not in "+-*/":
                return int(t)
            
            num2=dfs()
            num1=dfs()

            if t == "+":
                return num1+num2
            elif t=="-":
                return num1-num2
            elif t=="*":
                return num1*num2
            elif t=="/":
                return int(num1/num2)
        
        return dfs()
        
        
        # stack
        # op = {
        #     "+": operator.add,
        #     "-": operator.sub,
        #     "/": operator.truediv,
        #     "*": operator.mul
        # }
        # res=[]

        # for t in tokens:
        #     if t not in op:
        #         res.append(t)
        #     else:
        #         num2=int(res.pop())
        #         num1=int(res.pop())
        #         res.append(op[t](num1,num2))
        # print(res)
        # return int(res[0])

                

                    