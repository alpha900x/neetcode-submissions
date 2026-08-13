class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        if len(s)==0:
            return True
        hp={'(':')','[':']','{':'}'}
        stack=[]
        for i in range(len(s)):
            if s[i]==')' or s[i]=='}' or s[i]==']':
                if len(stack)==0 or s[i]!=hp[stack.pop()]:
                    return False
            else:
                stack.append(s[i])
                
        if len(stack)!=0:
            return False
        return True

            