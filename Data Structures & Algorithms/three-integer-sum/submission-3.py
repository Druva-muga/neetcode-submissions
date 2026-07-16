class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and nums[i-1] == nums[i]:
                continue
            if nums[i]>0:
                break
            l,r = i+1,len(nums)-1
            while l<r:
                target = a+nums[l]+nums[r]
                if 0>target:
                    l+=1
                elif 0<target:
                    r-=1
                else:
                    result.append([nums[l],nums[r],a])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1] :
                        l+=1
        return result

        