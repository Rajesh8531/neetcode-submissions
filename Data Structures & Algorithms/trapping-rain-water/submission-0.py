class Solution:
    def trap(self, nums: List[int]) -> int:
        solution = 0
        for i in range(len(nums)):
            leftMax = rightMax = nums[i]
            for j in range(i):
                leftMax = max(leftMax,nums[j])
            for k in range(i+1,len(nums)):
                rightMax = max(rightMax,nums[k])
            solution += min(leftMax,rightMax) - nums[i]
        return solution
        