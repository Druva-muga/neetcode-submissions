class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftmul = []
        rightmul = []
        result = []
        multsum = 1
        for i in range(0,len(nums)):
            multsum *= nums[i]
            leftmul.append(multsum)
        multsum = 1
        for i in range(len(nums)-1,-1,-1):
            multsum *= nums[i]
            rightmul.insert(0,multsum)
        print(leftmul,rightmul)
        for i in range(len(nums)):
            if i == 0:
                result.append(rightmul[i+1])
            elif i == len(nums)-1:
                result.append(leftmul[i-1])
            else:
                result.append(leftmul[i-1]*rightmul[i+1])

        return result
        