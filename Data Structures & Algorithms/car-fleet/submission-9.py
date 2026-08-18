class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            time=(target-position[i])/speed[i]
            position[i]=[position[i],time]
        position=sorted(position,key=lambda x:x[0],reverse=True)
        f_c=1
        f=position[0][1]
        for i in range(1,len(position)):
            if  position[i][1]>f:
                f=position[i][1]
                f_c+=1
        
        return f_c