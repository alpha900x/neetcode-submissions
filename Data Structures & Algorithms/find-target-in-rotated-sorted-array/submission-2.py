class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0]>nums[-1]:
            l,h = 0,len(nums)-1
            pivot = [0,float("inf")]
            while l<=h:
                m = (l+h)//2
                if nums[m]>=nums[0]:
                    l = m+1
                else:
                    h = m-1
                    if nums[m]<pivot[1]:
                        pivot[0] = m
        
            if target in range(nums[pivot[0]],nums[0]):
                l = pivot[0]
                h = len(nums)-1
            else:
                l = 0
                h = pivot[0]-1
            #print(l,h)
            while l<=h:
                m = (l+h)//2
                #print(m)
                if nums[m]>target:
                    h = m-1
                elif nums[m]<target:
                    l = m+1
                else:
                    return m
            return -1
        else:
            l,h = 0,len(nums)-1
            while l<=h:
                m = (l+h)//2
                if nums[m]<target:
                    l = m+1
                elif nums[m]>target:
                    h = m-1
                else:
                    return m
            return -1

        
        

                
                


