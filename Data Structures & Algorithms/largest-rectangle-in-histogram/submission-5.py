class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        s =  []
        for i,h in enumerate(heights):
            start = i
            while s and s[-1][1]>h:
                index,height = s.pop()
                area = max(area , height*(i-index))
                start = index
            s.append((start,h))
        
        for i,h in s:
            area = max(area , h*(len(heights)-i))
        return area   

                

                
            
