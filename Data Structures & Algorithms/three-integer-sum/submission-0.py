class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        op=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            t=-(nums[i])
            while j<k:
                if nums[j]+nums[k]>t:
                    k-=1
                elif nums[j]+nums[k]<t:
                    j+=1
                else:
                    sol=[nums[i],nums[j],nums[k]]
                    op.append(sol)
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                    while nums[k]==nums[k+1] and j<k:           
                        k-=1
                    
        return op   