class Solution:
    def findMin(self, nums: List[int]) -> int:
            if nums[0]>nums[-1]:
                l=0 
                h=len(nums)-1
                while l<=h:
                    m = (l+h)//2
                    if nums[m]>=nums[0]:
                        l=m+1  
                    else:
                        h=m-1
                        if nums[m]<=nums[h]:
                            return nums[m]
                return nums[m]
            return nums[0]
        


