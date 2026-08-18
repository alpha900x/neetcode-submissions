class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            time=(target-position[i])/speed[i]
            position[i]=[position[i],time]
        position=sorted(position,key=lambda x:x[0],reverse=True)
        stack=[]
        for i in range(len(position)):
            stack.append(position[i])
            if len(stack)>1 and stack[-1][1]<=stack[-2][1]:
                stack.pop()
        print(stack)
        return len(stack)