class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productAfter = [1] * len(nums)
        productAfter = [1] * len(nums)
        length = len(nums)
        for i in range(length-2,-1,-1):
            productAfter[i] = nums[i+1] * productAfter[i+1]

        productBefore = [1] * len(nums)
        for i in range(1,len(nums)):
            productBefore[i] = nums[i-1] * productBefore[i-1]

        res = []
        for i in range(len(nums)):
            res.append(productAfter[i]*productBefore[i])
        return res