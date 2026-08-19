class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = heights
        a=0
        rs=[0]
        rmax=[0]*len(h)
        for i in range(1,len(h)):
            while rs and h[rs[-1]]>h[i]:
                ind = rs.pop()
                rmax[ind] = (i-ind)
            rs.append(i)
        for i in rs:
            rmax[i]=rs[-1]-i+1
        
        ls=[len(h)-1]
        lmax=[0]*len(h)
        for i in range(len(h)-2,-1,-1):
            while ls and h[ls[-1]]>h[i]:
                ind = ls.pop()
                lmax[ind] = (ind-i)
            ls.append(i)
        for i in ls:
            lmax[i]=i+1
        
        for i in range(len(h)):
            area = h[i]*(rmax[i]+lmax[i]-1)
            if a<area:
                a = area
        return a
        

                

                
            
