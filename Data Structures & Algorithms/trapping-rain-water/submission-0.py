class Solution:
    def trap(self, height: List[int]) -> int:
        w=0

        #left
        left=[]
        for j in range(len(height)):
            if j==0:
                left.append(0)
                continue
            if left[j-1]<height[j-1]:
                left.append(height[j-1])
            else:
                left.append(left[j-1])
        
        #right
        right=[0]*len(height)
        for j in range(len(height)-1,-1,-1):
            if j==len(height)-1:
                right[j]=0
                continue
            if right[j+1]<height[j+1]:
                right[j]=height[j+1]
            else:
                right[j]=right[j+1]
             

        for i in range(len(height)):
            if min(left[i],right[i])>=height[i]:
                w+=min(left[i],right[i])-height[i]
           

        return w  
               



