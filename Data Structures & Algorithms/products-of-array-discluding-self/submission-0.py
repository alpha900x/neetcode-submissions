class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op=[1]*len(nums) 
        hp={}
        r,l=1,1
        for i in range(len(nums)-1):
            j=len(nums)-i-1
            l*=nums[i]
            r*=nums[j]
            op[i+1]*=l
            op[j-1]*=r
        return op   