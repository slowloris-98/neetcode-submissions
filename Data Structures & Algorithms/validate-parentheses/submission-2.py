class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for b in s:
            if b in ('(', '[', '{'):
                stack.append(b)
            elif b in (')', ']', '}') and not stack:
                return False
            else:
                if b == ')' and stack[-1]!='(':
                    return False
                elif b == ']' and stack[-1]!='[':
                    return False
                elif b == '}'and stack[-1]!='{':
                    return False
                stack.pop()
        return True if not stack else False
