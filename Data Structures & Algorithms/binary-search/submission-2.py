class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h=len(nums)-1
        l=0
        while l<=h:
            mid=(h+l)//2
            if nums[mid]>target:
                h=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                return mid
        return -1