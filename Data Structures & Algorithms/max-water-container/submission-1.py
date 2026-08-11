class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==1 or len(height)==0:
            return 0
        maxw=0
        i=0
        j=len(height)-1

        while i<j:
            w=min(height[i],height[j])*(j-i)
            if w > maxw:
                maxw=w
            if height[i]>=height[j] :
                j-=1
            else:
                i+=1
                    
        return maxw
                   


    

         
