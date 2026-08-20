import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack
        op = {
            "+": operator.add,
            "-": operator.sub,
            "/": operator.truediv,
            "*": operator.mul
        }
        res=[]

        for t in tokens:
            if t not in op:
                res.append(t)
            else:
                num2=int(res.pop())
                num1=int(res.pop())
                res.append(op[t](num1,num2))
        print(res)
        return int(res[0])

                

                    