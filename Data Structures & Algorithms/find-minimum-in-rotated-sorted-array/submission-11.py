class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]>nums[-1]:
            l=0 
            h=len(nums)-1
            pos = 0
            while l<=h:
                m = (l+h)//2
                if nums[m]>=nums[0]:
                    l=m+1  
                elif nums[m]<nums[0]:
                    h=m-1
                    if nums[m] < nums[pos]:
                        pos = m
                else:
                    break
            return nums[pos]
        return nums[0]


