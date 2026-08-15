class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                b=stack.pop()
                a=stack.pop()
                stack.append(a+b)
               # print(stack[-1])
            elif i=="-":
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
               #print(stack[-1])

            elif i=="*":
                b=stack.pop()
                a=stack.pop()
                stack.append(a*b)
               # print(stack[-1])

            elif i=="/":
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b))
               # print(stack[-1])

            else:
                stack.append(int(i))
               # print(i)
        return (stack[0])
            

        