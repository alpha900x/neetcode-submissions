class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h=len(nums)-1
        l=0
        mid=(h+l)+1//2
        print(mid)
        while l<=h:
            if nums[mid]>target:
                h=mid-1
                mid=(h+l)//2
                print(h,mid,l)
            elif nums[mid]<target:
                l=mid+1
                mid=(h+l)//2
                print(h,mid,l)
            else:
                return mid
                print(h,mid,l)
        return -1