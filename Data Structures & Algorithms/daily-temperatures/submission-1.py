class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures)==0 or len(temperatures)==1:
            return [0]
        op=[0]*len(temperatures)
        stack=[0]
        
        for i in range(1,len(temperatures)):
            if temperatures[stack[-1]]<temperatures[i]:
                while stack and temperatures[stack[-1]]<temperatures[i]:
                    indice = stack.pop()
                    op[indice] = i-indice
            stack.append(i)
        
        
        return op       
                
                