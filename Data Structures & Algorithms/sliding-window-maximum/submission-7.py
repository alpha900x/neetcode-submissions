class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i,j = 0,k-1
        maxs = []
        max_ind,max_val = max(enumerate(nums[i:j+1]),key = lambda x:x[1])
        cnt = max_ind 
        while j<len(nums):
            # max logic
            if nums[j]>max_val:
                cnt = 0
                max_val = nums[j]
                maxs.append(max_val)
            else:
                if cnt == 0:
                    max_ind,max_val = max(enumerate(nums[i:j+1]),key = lambda x:x[1])
                    cnt = max_ind
                    maxs.append(max_val)
                else:
                    maxs.append(max_val)
                    cnt-=1
            i+=1
            j+=1
        return maxs