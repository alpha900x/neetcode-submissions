from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxs=[]
        d = deque(maxlen = len(nums))
        i,j = 0,k-1
        d.append(0)
        for num in range(i+1,j+1):
            if nums[num]>nums[d[-1]]:
                while d and nums[num]>nums[d[-1]]:
                    d.pop()
                d.append(num)
            else:
                d.append(num)
        maxs.append(nums[d[0]])
        while j<len(nums)-1:
            i+=1
            j+=1
            if d[0]<i:
                d.popleft()
            while d and nums[j]>nums[d[-1]]:
               d.pop()
            d.append(j)
            maxs.append(nums[d[0]])
        return maxs

            



        